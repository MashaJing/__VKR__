import eegraph

G = eegraph.Graph()
G.load_data(path = 'data\\S001R01.edf', exclude = ['EEG TAntI1-TAntI', 'EEG TAntD1-TAntD', 'EEG EKG1-EKG2'])
graphs, connectivity_matrix = G.modelate(window_size = 2, connectivity = 'squared_coherence', bands = ['delta','theta','alpha'])
print(connectivity_matrix)