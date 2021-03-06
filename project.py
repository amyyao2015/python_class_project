import pandas as pd
schldata = pd.read_csv("schoolzip.csv", usecols = ['dbn','school_name','boro','graduation_rate',\
                                                    'attendance_rate','pct_stu_enough_variety',\
                                                    'college_career_rate','pct_stu_safe','Postcode'])
schldata = schldata.rename(columns = {'pct_stu_enough_variety':'variety_rate','pct_stu_safe':'safety_rate'})
schldata = schldata.fillna(schldata.mean())
