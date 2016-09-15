import numpy as np
import matplotlib.pyplot as plt
import bootcamp_utils as bc_ut
import pandas as pd
import seaborn as sns
sns.set()

df_drones= pd.read_csv('../data/bee_weight.csv', comment='#')

df_control_w= df_drones.loc[(df_drones['Treatment']== 'Control'), 'Weight']
df_pest_w= df_drones.loc[(df_drones['Treatment']== 'Pesticide'), 'Weight']

#Calculate the ECDF
c_w_x, c_w_y= bc_ut.ecdf(df_control_w)
p_w_x, p_w_y= bc_ut.ecdf(df_pest_w)

#Plot the ECDF
plt.plot(c_w_x, c_w_y, marker='.', markersize=5, linestyle='none')
plt.plot(p_w_x, p_w_y, marker='.', markersize=5, linestyle='none')
plt.xlabel('bee weight')
plt.ylabel('ECDF')
plt.show()

#Compute the mean
df_c_w_mean = np.mean(df_control_w)
df_p_w_mean = np.mean(df_pest_w)

#Compute 95% confidence intervals
confint95_c_w= bc_ut.confinterval95(df_control_w, np.mean, size=100000)
confint95_p_w= bc_ut.confinterval95(df_pest_w, np.mean, size=100000)

###Repeat a-c but for drone sperm
#There is a nan, so you must remove it
df_drones_quality= pd.read_csv('../data/bee_sperm.csv', comment='#')
df_drones_quality= pd.DataFrame.dropna(df_drones_quality)

df_control_q= df_drones_quality.loc[(df_drones_quality['Treatment']== 'Control'), 'Quality']
df_pest_q= df_drones_quality.loc[(df_drones_quality['Treatment']== 'Pesticide'), 'Quality']

#Calculate the ECDF
c_q_x, c_q_y= bc_ut.ecdf(df_control_q)
p_q_x, p_q_y= bc_ut.ecdf(df_pest_q)

#Plot the ECDF
plt.plot(c_q_x, c_q_y, marker='.', markersize=5, linestyle='none')
plt.plot(p_q_x, p_q_y, marker='.', markersize=5, linestyle='none')
plt.xlabel('bee weight')
plt.ylabel('ECDF')
plt.show()

#Compute the mean
df_c_q_mean = np.nanmean(df_control_q)
df_p_q_mean = np.nanmean(df_pest_q)

#Compute 95% confidence intervals

confint95_c_q= bc_ut.confinterval95(df_control_q, np.mean, size=100000)
confint95_p_q= bc_ut.confinterval95(df_pest_q, np.mean, size=100000)

#Compute 95% Conf interval for median

confint95_c_q_median= bc_ut.confinterval95(df_control_q, np.median, size=100000)
confint95_p_q_median= bc_ut.confinterval95(df_pest_q, np.median, size=100000)
