import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt
import argparse
import os

def main(args):
    dataset = pd.read_csv(os.path.join('drug200.csv'))
    dataset['Sex'] = dataset['Sex'].map({'F':0,'M':1})
    dataset['BP'] = dataset['BP'].map({'HIGH':0,'LOW':1,'NORMAL':2})
    dataset['Cholesterol'] = dataset['Cholesterol'].map({'HIGH':0,'NORMAL':1})
    dataset['Drug'] = dataset['Drug'].map({'drugA':0,'drugB':1,'drugC':2,'drugX':3,'DrugY':4})
    
    x = dataset.iloc[:,:-1]
    y = dataset.iloc[:,-1]
    
    X_train, x_test, Y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    Drug_classification = DecisionTreeClassifier(max_leaf_nodes=10,random_state=0)
    print(f"{5*'#'}Training{5*'#'}")
    Drug_classification.fit(X_train,Y_train)
    fig = plt.figure(figsize=(25,20))
    _ = tree.plot_tree(Drug_classification)
    fig.savefig(os.path.join("decistion_tree.png"))
    print("decistion_tree saved.")
    
    
    print(f"{5*'#'}Testing{5*'#'}")
    y_predicted = Drug_classification.predict(x_test)
    
    print(f"Accuracy on testset: {accuracy_score(y_test,y_predicted)*100}%")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input", default="./drug200.csv", help="data set path")
    parser.add_argument('-o', "--output", default=".", help="The address of the tree output file storage location")
    args = parser.parse_args()
    main(args)