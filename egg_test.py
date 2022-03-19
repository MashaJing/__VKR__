import eegraph

bands = ['alpha','beta','gamma','delta','theta']
# for i in bands:
G = eegraph.Graph()
G.load_data(path = 'data/S001R01.edf', exclude = [
'Fc5.', 'Fc3.', 'Fc1.', 'Fcz.', 'Fc2.',
'Fc4.', 'Fc6.', 'C5..', 'C3..', 'C1..',
        'C2..', 'C4..', 'C6..', 'Cp5.',
'Cp3.', 'Cp1.', 'Cpz.', 'Cp2.', 'Cp4.',
'Fp1.', 'Fpz.', 'Fp2.', 'Af7.', 'Af3.',
'Afz.', 'Af4.', 'Af8.', 'F7..', 'F5..',
'F3..', 'F1..',         'F2..', 'F4..', 
'F6..', 'F8..', 'Ft7.', 'Ft8.', 'T7..', 
'T8..', 'T9..', 'T10.', 'Tp7.', 'Cp6.',
'Tp8.', 'P7..', 'P5..', 'P3..', 'P1..', 
'P2..', 'P4..', 'P6..', 'P8..', 'Po7.',
'Po3.', 'Poz.', 'Po4.', 'Po8.',   
'O1..',         'O2..', 'Iz..'])
print(G.ch_names)
# G.load_data(path = 'data/S001R01.edf', exclude = ['EEG TAntI1-TAntI', 'EEG TAntD1-TAntD', 'EEG EKG1-EKG2'])
graphs, connectivity_matrix = G.modelate(window_size = 200, connectivity = 'squared_coherence', bands=bands)
G.visualize(graphs[0], f'graph_1')

"""
1. Какие электроды необходимо исключать?
2. Написать даме, чтоб кинула скрипт
3. Построить какой-нибудь уже граф
"""

# standard_electrodes = ['Cz', 'Pz', 'Oz', 'Fz', 'Nz']
