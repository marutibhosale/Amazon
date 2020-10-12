import pickle
import numpy as np


class Classifier:
    def __init__(self, data_point):                      # define constructor
        self.data_point = data_point

    def ohe_value(self):                                   # Define instance method for one hot encoding
        pkl_filename = 'static/pickle_OHE.pkl'
        with open(pkl_filename, 'rb') as file:
            ohe_pickle = pickle.load(file)                 # load pickle file
        vector = np.array(list(self.data_point.values()))  # convert to array
        vector = vector.reshape(1, -1)                     # reshape(1,-1)
        ohe_vector = ohe_pickle.transform(vector)          # apply one hot encoding
        return ohe_vector                                  # return one hot encoded vector

    def classify(self):                                    # define instance method for predict class label
        vector_ohe = self.ohe_value()               # call ohe_value method which return one hot encoded vector
        pkl_filename = 'static/pickle_model.pkl'
        with open(pkl_filename, 'rb') as file:     # open pickle file in read binary mode
            model = pickle.load(file)              # loading pickle file content pre trained machine learning model
        predict = model.predict(vector_ohe)        # predicting class label
        if predict == 1:                           # if label=1 return access is Approved else return access is denied
            access = 'Approved'
        else:
            access = 'Denied'
        access_dict = dict()             # define empty dictionary
        access_dict['status'] = access   # updating status in dictionary format
        return access_dict               # return predicated access status