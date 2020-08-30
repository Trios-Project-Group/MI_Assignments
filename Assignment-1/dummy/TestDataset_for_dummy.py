from Assignment_1 import *   

def test_case():
    df = pd.read_csv("dummy.csv")
    try:
        if get_entropy_of_dataset(df) >=0.988 and get_entropy_of_dataset(df)<=0.989:
            print("Test Case 1 for the function get_entropy_of_dataset PASSED")
            print(get_entropy_of_dataset(df))
        else:
            print("Test Case 1 for the function get_entropy_of_dataset FAILED")
    except:
        print("Test Case 1 for the function get_entropy_of_dataset FAILED")
    
    try:
        if get_entropy_of_attribute(df,'Color')>=0.953 and get_entropy_of_attribute(df,'Color')<=0.954 :
            print("Test Case 2 for the function get_entropy_of_attribute PASSED")
            print(get_entropy_of_attribute(df,'Color'))
        else:
            print("Test Case 2 for the function get_entropy_of_attribute FAILED")
            
    except:
         print("Test Case 2 for the function get_entropy_of_attribute FAILED")
        
    try:
        if get_entropy_of_attribute(df,'Size')>=0.882 and get_entropy_of_attribute(df,'Size')<=0.883:
            print("Test Case 3 for the function get_entropy_of_attribute PASSED")
            print(get_entropy_of_attribute(df,'Size'))
        else:
            print("Test Case 3 for the function get_entropy_of_attribute FAILED")
            
    except:
        print("Test Case 3 for the function get_entropy_of_attribute FAILED")
        
    try:
        ans=get_selected_attribute(df)
        #dictionary=ans[0]
        print(ans)
    except:
        print("Test Case 4 for the function get_selected_attribute FAILED")
    

if __name__=="__main__":
	test_case()

