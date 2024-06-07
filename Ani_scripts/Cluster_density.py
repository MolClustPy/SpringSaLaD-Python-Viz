# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:43:43 2021

@author: Ani Chattaraj
"""

from DataPy import ReadInputFile, InterSiteDistance, ProgressBar, displayExecutionTime
import re, json, pickle
import numpy as np
import networkx as nx
from glob import glob
import matplotlib.pyplot as plt
from csv import writer
from numpy import pi
from collections import defaultdict, OrderedDict, namedtuple

def connected_component_subgraphs(G):
    for c in nx.connected_components(G):
        yield G.subgraph(c)
# pos = center of mass, radius = Radius of gyration, 
#density = sites/volume
Cluster = namedtuple('Cluster', ['pos', 'radius', 'density'])

class ClusterDensity:

    def __init__(self, txtfile):
        self.simObj = ReadInputFile(txtfile)
        tf, dt, dt_data, dt_image = self.simObj.getTimeStats()
        inpath = self.simObj.getInpath() + "/data"
        numRuns = self.simObj.getNumRuns()
        self.N_frames = int(tf/dt_image)
        self.inpath = inpath
        self.numRuns = numRuns

    def __repr__(self):
        simfile = self.simObj.txtfile.split('/')[-1]
        info = f"Class : {self.__class__.__name__}\nSystem : {simfile}"
        return info

    @staticmethod
    def getMolIds(molfile, molName):
        molDict = {}
        mIds = []
        with open(molfile, 'r') as tmpfile:
            for line in tmpfile:
                line = line.strip().split(',')
                if line[-1] == molName:
                    mIds.append(line[0])
        molDict[molName] = mIds
        return molDict

    @staticmethod
    def getSiteIds(sitefile, molName):
        siteDict = {}
        sIds = []
        with open(sitefile, 'r') as tmpfile:
            for line in tmpfile:
                line = line.strip().split(',')
                if line[-1].split()[0] == molName:
                    sIds.append(line[0])
        siteDict[molName] = sIds
        return siteDict

    @staticmethod
    def getRevDict(myDict):
        # k,v = key : [val1, val2, ...]
        revDict = {}
        for k,v in myDict.items():
            for val in v:
                revDict[val] = k
        return revDict
    @staticmethod
    def splitArr(arr, n):
        subArrs = []
        if (len(arr)%n == 0):
            f = int(len(arr)/n)
            i = 0
            while (i < len(arr)):
                sub_arr = arr[i : i+f]
                i += f
                subArrs.append(sub_arr)
            return subArrs
        else:
            print(f"Can't split the given array (length = {len(arr)}) into {n} parts")

    def mapSiteToMolecule(self):
        sIDfile = InterSiteDistance.findFile(self.inpath, self.numRuns, "SiteIDs")
        mIDfile = InterSiteDistance.findFile(self.inpath, self.numRuns, "MoleculeIDs")
        molName, molCount = self.simObj.getMolecules()
        molIDs, siteIDs = {}, {}
        for mol in molName:
            molIDs.update(self.getMolIds(mIDfile, mol))
            siteIDs.update(self.getSiteIds(sIDfile, mol))
        spmIDs = {} # sites per molecule
        for mol, count in zip(molName, molCount):
            #molDict = {}
            arr = self.splitArr(siteIDs[mol], count)
            mol_ids = molIDs[mol]
            d = dict(zip(mol_ids, arr))
            spmIDs.update(d)
        rev_spm = self.getRevDict(spmIDs)
        return rev_spm

    @staticmethod
    def getBindingStatus(frame):
        linkList = []
        posDict = {}
        for curline in frame:
            if re.search("ID", curline):
                line = curline.split()
                posDict[line[1]] = [float(line[4]),float(line[5]), float(line[6])] # order = x,y,z
                #IdList.append(line.split()[1])

            if re.search("Link", curline):
                line = curline.split()
                linkList.append((line[1], line[3]))
        return posDict, linkList

    @staticmethod
    def createGraph(IdList, LinkList):
        G = nx.Graph()
        G.add_nodes_from(IdList)
        G.add_edges_from(LinkList)
        return G

    @staticmethod
    def getFrameIndices(viewerfile):
        frame_indices = []
        tps = []
        with open(viewerfile, 'r') as tmpfile:
            lines = tmpfile.readlines()
            for i, line in enumerate(lines):
                if re.search("SCENE", line):
                    frame_indices.append(i)
                    tp = lines[i+1].split()[-1]
                    tps.append(tp)

            frame_indices.append(len(lines))

        return tps, frame_indices

    @staticmethod
    def calc_RadGy(posList):
        # posList = N,3 array for N sites
        com = np.mean(posList, axis=0) # center of mass
        Rg2 = np.mean(np.sum((posList - com)**2, axis=1))
        return com, np.sqrt(Rg2)

    def getClusterDensity(self, viewerfile):
        #SD, MD: site density, molecular density (number/Rg**3)
        SD_list = []
        MD_list = []
        clusList = []
        msm = self.mapSiteToMolecule()
        completeTrajectory = False
        tps, frame_indicies = self.getFrameIndices(viewerfile)
        index_pairs = []
        c2d_map = defaultdict(list)
        for i in range(len(frame_indicies)-1):
            index_pairs.append((frame_indicies[i],frame_indicies[i+1]))

        if len(tps) != self.N_frames + 1:
            pass
        else:
            completeTrajectory = True

            with open(viewerfile, 'r') as infile:
                lines = infile.readlines()
                for i,j in index_pairs:
                    current_frame = lines[i:j]
                    cluster_index = 0
                    posDict, Links = self.getBindingStatus(current_frame)
                    Ids = [_ for _ in posDict.keys()]
                    mIds, mLinks = [msm[k] for k in Ids], [(msm[k1], msm[k2]) for k1,k2 in Links]
                    sG = self.createGraph(Ids, Links)
                    mG = self.createGraph(mIds, mLinks)
                    tmp_sd, tmp_md = [], []
                    clusters = []

                    #G.subgraph(c) for c in connected_components(G)
                    for sg, mg in zip(connected_component_subgraphs(sG), connected_component_subgraphs(mG)):
                        #print(f"cluster {cluster_index}")
                        cluster_index += 1
                        sites = list(sg.nodes)
                        mols = list(mg.nodes)
                        site_pairs = list(sg.edges())
                        posList = np.array([posDict[s] for s in sites])
                        #print(posList)
                        com, Rg = self.calc_RadGy(posList)
                        
                        #ClusterPos.append((com,Rg))
                        #print(f'cluster = {cluster_index}, sites = {len(sites)}, Rg = {Rg}')
                        sd, md = len(sites)/((4/3)*pi*Rg**3), len(mols)/((4/3)*pi*Rg**3)
                        c2d_map[len(mols)].append(sd)
                        clusters.append(Cluster(pos=com, radius=Rg, density=sd))
                        tmp_sd.append(sd)
                        tmp_md.append(md)
                    clusList.append(clusters)
                    SD_list.append(np.mean(np.array(tmp_sd)))
                    MD_list.append(np.mean(np.array(tmp_md)))



        if completeTrajectory:
            return SD_list, MD_list, c2d_map, clusList
        else:
            return None

    @displayExecutionTime
    def getCD_stat(self):
        sysName = self.inpath.split('/')[-2].replace('_SIM_FOLDER','')
        print('\nSystem: ', sysName)
        print("Calculating Cluster density ...")
        SD_list, MD_list = [], []
        c2d_map = defaultdict(list)
        #clusPosList = []

        outpath = self.simObj.getOutpath("Cluster_density_stat")
        vfiles = glob(self.simObj.getInpath() + "/viewer_files/*.txt")[:]

        IVF = [] # Incomplete Viewer File
        N_traj = len(vfiles)
        Runs = []

        for i, vfile in enumerate(vfiles):
            res = self.getClusterDensity(vfile)
            runNum = vfile.split('_')[-1].replace('.txt','')
            #print(f'Run = {runNum}')
            if res == None:
                IVF.append(runNum)
            else:
                Runs.append(runNum)
                SD_list.append(res[0])
                MD_list.append(res[1])
                #np.savetxt(outpath + "/{runNum}_clusterPos.txt", res[3])
                #for j, elem in enumerate(res[3]):
                    #pickle.dump(elem, open(outpath+f"/{runNum}_Frame_{j+1}.pickle", mode="wb"))
                
                for k,v in res[2].items():
                    c2d_map[k].append(v)
            ProgressBar("Progress", (i+1)/N_traj)
       
        
        tf, dt, dt_data, dt_image = self.simObj.getTimeStats()
        timeSeries = np.arange(0,tf+dt_image, dt_image)
        SD_data, MD_data = [timeSeries], [timeSeries]
        mean_SD, mean_MD = np.mean(np.array(SD_list), axis=0), np.mean(np.array(MD_list), axis=0)
        #print(mean_SD)
        mean_arr = np.stack((timeSeries, mean_SD, mean_MD), axis=1)
        for e1,e2 in zip(SD_list, MD_list):
            SD_data.append(e1)
            MD_data.append(e2)

        #header = ['Time(s)'] + Runs
        #header = ','.join(header)
        #np.savetxt(outpath + "/site_density.csv", np.array(SD_data).T, delimiter=',', header=header)
        #np.savetxt(outpath + "/molecular_density.csv", np.array(MD_data).T, delimiter=',', header=header)

        head02 = 'Time(s),mean_SD,mean_MD'
        np.savetxt(outpath + "/Density_timecourse.csv", mean_arr, delimiter=',', header=head02)
        json.dump(c2d_map, open(outpath+'\cluster_density_map.json','w'))
        


for cb in [25,55,75,104,125,138,150,166,184,205,256]:
#for cb in [104]:
    txtfile = f'Y:/Ani_Chattaraj/eLife_2021_Ksp_data/Figure07/00_Reference_system/4v_4v_flex_9nm_linker_SIMULATIONS/4v_flex_config03_CB_{cb}uM_SIM_FOLDER/4v_flex_config03_CB_{cb}uM_SIM.txt'
    cd = ClusterDensity(txtfile)
    cd.getCD_stat()
