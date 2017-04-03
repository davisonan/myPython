#' % Predicting bad loans
#' % Xu Tian
#' % 2017/04/03


#' # Background


#' Exploratory data analysis
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score

path = '/Users/hanya/Documents/01_Work/01_Projects/01_Global_Atlantic/00_Loans/00_Yhat/'

df1 = pd.read_csv(path + 'data/df_2016Q1.csv')

# Eveyr loan has a unique ID
len(df1['id'].unique()) == df1.shape[0]

# Eveyr loan has a unique member ID
len(df1['member_id'].unique()) == df1.shape[0]

# Summary statisitics of loan_amnt
df1['loan_amnt'].describe(percentiles=[0.01, 0.05, 0.95, 0.99])

# Summary statisitics of funded_amnt
df1['funded_amnt'].describe(percentiles=[0.01, 0.05, 0.95, 0.99])

# All the loan_amnt is equal to the funded_amnt, i.e., if funded, the loan_amnt
# is fully funded.
sum(df1['loan_amnt'] == df1['funded_amnt']) == df1.shape[0]

# Loan funded by investors.
sum(df1['funded_amnt_inv'] == df1['funded_amnt']) == df1.shape[0]

# All the loans funded by investors are smaller or equal to the funded_amnt
sum(df1['funded_amnt_inv'] <= df1['funded_amnt']) == df1.shape[0]

# 94.4% of the loans are fully funded by investors
n_funded_amnt_int = sum(df1['funded_amnt_inv'] == df1['funded_amnt'])
n_funded_amnt_int / df1.shape[0]

# On average, -133 short
sum(df1['funded_amnt_inv'] - df1['funded_amnt']) / (df1.shape[0] - n_funded_amnt_int)

# Number of terms: 36 months versus 60 months, 71.8% former, 28.2% latter.
df1.groupby(['term']).agg('count')['id']

df1['int_rate'].apply(lambda x: float(x[:-1]) / 100).describe()
# mean          0.124771
# std           0.048289
# min           0.053200
# 25%           0.084900
# 50%           0.119900
# 75%           0.153100
# max           0.289900

int_rate = df1['int_rate'].apply(lambda x: float(x[:-1]) / 100)

plt.figure('int_rate')
plt.subplot(211)
plt.plot(sorted(int_rate))
plt.subplot(212)
plt.hist(int_rate, bins=20)

# Installment: monthly payments
df1['installment'].describe()


# Can be improved with numbers of ticks
def drawValCounts(x, name, rotation=0):
    """Function to draw count values""""
    n = len(x)
    x_pos = np.arange(n)
    keys = x.keys()
    vals = x.values
    plt.figure()
    plt.bar(x_pos, vals, align='center', alpha=0.75)
    plt.xticks(x_pos, keys, rotation=rotation)
    plt.ylabel('Counts')
    plt.title('Counts by ' + name)


# Grade: LC assigned loan grade
df1['grade'].value_counts()
drawValCounts(df1['grade'].value_counts(), 'loan grades')


# Subgrades:
df1['sub_grade'].value_counts()
subgrades = df1['sub_grade'].value_counts().keys()
x_pos = np.arange(len(subgrades))
values = df1['sub_grade'].value_counts().values
plt.figure('Loan sub_grades barplot')
plt.bar(x_pos, values, align='center', alpha=0.75)
plt.xticks(x_pos, subgrades, rotation='vertical')
plt.ylabel('Counts')
plt.title('Counts by loan sub_grades')

# emp_length
df1['emp_length'].value_counts()


# home_ownership
df1['home_ownership'].value_counts()

# annual_inc
df1['annual_inc'].describe(percentiles=[0.01, 0.05, 0.95, 0.99])

# verification_status
df1['verification_status'].value_counts()


# issue_d: Jan, Feb, Mar in 2016
df1['issue_d'].value_counts()

# loan_status
df1['loan_status'].value_counts()
bad_indicators = set(['Late (16-30 days)', 'Late (31-120 days)', 'Default', 'Charged Off'])
iBad = df1['loan_status'].apply(lambda x: x in bad_indicators)  # responss variable


# pymnt_plan: indicates if a payment plan has been put in place for the loan
df1['pymnt_plan'].value_counts()

# purpose: A category provided by the borrower for the loan request.
df1['purpose'].value_counts()

# title
df1['title'].value_counts()

# zip_code
df1['zip_code'].head()

# addr_state
df1['addr_state'].value_counts()

# dti: debt to income ratio, excluding some specifics
dti = df1['dti']/100

# delinq_2yrs
df1['delinq_2yrs'].value_counts()

# earliest_cr_line
df1['earliest_cr_line'].value_counts()

# Calcuating the length of credit history before applying for the loan
dts1 = pd.to_datetime(df1['issue_d'], format="%b-%y")
dts2 = [i[:-2] + '19' + i[-2:] if 20 < int(i[-2:]) else i[:-2] + '20' + i[-2:] for i in df1['earliest_cr_line']]
dts2 = pd.to_datetime(dts2, format='%b-%Y')
lenCreditHistory = [(dts1[i] - dts2[i]).days for i in range(len(dts1))]

# inq_last_6mths
df1['inq_last_6mths'].describe()
df1['inq_last_6mths'].value_counts()

# mths_since_last_delinq
df1['mths_since_last_delinq'].describe()
df1['mths_since_last_delinq'].value_counts()

# mths_since_last_record: since last public record
df1['mths_since_last_record'].describe()
df1['mths_since_last_record'].value_counts()

# open_acc
df1['open_acc'].describe()
drawValCounts(df1['open_acc'].value_counts(), 'open accounts', rotation='vertical')

# pub_rec: number of derogatory public records
df1['pub_rec'].describe()
df1['pub_rec'].value_counts()

# revol_bal: number of derogatory public records
df1['revol_bal'].describe()

# revol_util
revol_util = df1['revol_util'].apply(lambda x: float(x[0][:-1])/100)

def f(x):
    if type(x) is float:
        return 0.0
    else:
        return float(x[:-1])

revol_util = pd.Series([f(i) for i in df1['revol_util']])
df1['revol_util2'] = revol_util

# total_acc
df1['total_acc'].describe()
df1['total_acc'].value_counts()

# initial_list_status
df1['initial_list_status'].value_counts()

# out_prncp: remaining outstanding principal
df1['out_prncp'].describe()

# out_prncp_inv
df1['out_prncp_inv'].describe()

# total_pymnt
df1['total_pymnt'].describe()

# total_pymnt
df1['total_pymnt_inv'].describe()

# total_rec_prncp: principal received to date
df1['total_rec_prncp'].describe()

# total_rec_int: interest received to date
df1['total_rec_int'].describe()

# total_rec_late_fee
df1['total_rec_late_fee'].describe()

# recoveries
df1['recoveries'].describe()

# collection_recovery_fee
df1['collection_recovery_fee'].describe()

# last_pymnt_d
df1['last_pymnt_d'].head()

# last_pymnt_amnt
df1['last_pymnt_amnt'].describe()

# next_pymnt_d
df1['next_pymnt_d'].head()

# last_credit_pull_d
df1['last_credit_pull_d'].head()

# collections_12_mths_ex_med
df1['collections_12_mths_ex_med'].describe()

# mths_since_last_major_derog
df1['mths_since_last_major_derog'].describe()

# policy_code
df1['policy_code'].value_counts()

# application_type
df1['application_type'].value_counts()

# acc_now_delinq
df1['acc_now_delinq'].value_counts()

# tot_coll_amt: total collection amount ever owed.
df1['tot_coll_amt'].value_counts()
df1['tot_coll_amt'].describe()

# tot_cur_bal:
df1['tot_cur_bal'].describe()

# open_acc_6m: number of open trades in the past 6 months
df1['open_acc_6m'].describe()
df1['open_acc_6m'].value_counts()
drawValCounts(df1['open_acc_6m'].value_counts(), 'open accounts in the past 6 months')

# open_il_6m: Number of currently active installment trades
df1['open_il_6m'].describe()
df1['open_il_6m'].value_counts()

#
df1['open_il_12m'].describe()
df1['open_il_12m'].value_counts()
drawValCounts(df1['open_il_12m'].value_counts(), 'active installment trades in the past 12 months')


#
df1['open_il_24m'].describe()
df1['open_il_24m'].value_counts()

df1['mths_since_rcnt_il'].describe()
df1['mths_since_rcnt_il'].value_counts()

df1['total_bal_il'].describe()
df1['total_bal_il'].value_counts()

df1['il_util'].describe()
df1['il_util'].value_counts()

# Number of revolving trades in the past 12 months
df1['open_rv_12m'].describe()
df1['open_rv_12m'].value_counts()

df1['open_rv_24m'].describe()
df1['open_rv_24m'].value_counts()

df1['max_bal_bc'].describe()
df1['max_bal_bc'].value_counts()

# balance to credict limit on all trades
df1['all_util'].describe()
df1['all_util'].value_counts()

# total revolving high credit/credit limit
df1['total_rev_hi_lim'].describe()

# Number of personal finance inquiries
df1['inq_fi'].describe()

# Number of finance trades
df1['total_cu_tl'].describe()

# Number of credit inquiries in past 12 months
df1['inq_last_12m'].describe()

# Number of trades opened in past 24 months.
df1['acc_open_past_24mths'].describe()

# Average current balance of all accounts
df1['avg_cur_bal'].describe()

# Total open to buy on revolving bankcards.
df1['bc_open_to_buy'].describe()

# Ratio of total current balance to high credit/credit limit for all bankcard accounts.
df1['bc_util'].describe()

# Number of charge-offs within 12 months
df1['chargeoff_within_12_mths'].describe()

# The past-due amount owed for the accounts on which the borrower is now delinquent.
df1['delinq_amnt'].describe()

# Months since oldest bank installment account opened
df1['mo_sin_old_il_acct'].describe()

# Months since oldest revolving account opened
df1['mo_sin_old_rev_tl_op'].describe()

# Months since most recent revolving account opened
df1['mo_sin_rcnt_rev_tl_op'].describe()

# Months since most recent account opened
df1['mo_sin_rcnt_tl'].describe()

# Number of mortgage accounts.
df1['mort_acc'].describe()
drawValCounts(df1['mort_acc'].value_counts(), 'mortgage accounts')

# Months since most recent bankcard account opened.
df1['mths_since_recent_bc'].describe()

# Months since most recent bankcard delinquency
df1['mths_since_recent_bc_dlq'].describe()

# Months since most recent inquiry.
df1['mths_since_recent_inq'].describe()
drawValCounts(df1['mths_since_recent_inq'].value_counts(), 'mths_since_recent_inq', 'vertical')

# Months since most recent revolving delinquency.
df1['mths_since_recent_revol_delinq'].describe()
df1['mths_since_recent_revol_delinq'].value_counts()

# Number of accounts ever 120 or more days past due
df1['num_accts_ever_120_pd'].describe()
drawValCounts(df1['num_accts_ever_120_pd'].value_counts(), 'num_accts_ever_120_pd', 'vertical')

# Number of currently active bankcard accounts
df1['num_actv_bc_tl'].describe()
drawValCounts(df1['num_actv_bc_tl'].value_counts(), 'num_actv_bc_tl', 'vertical')

# Number of currently active revolving trades
df1['num_actv_rev_tl'].describe()
drawValCounts(df1['num_actv_rev_tl'].value_counts(), 'num_actv_rev_tl', 'vertical')

# Number of satisfactory bankcard accounts
df1['num_bc_sats'].describe()
drawValCounts(df1['num_bc_sats'].value_counts(), 'num_bc_sats', 'vertical')

# Number of bankcard accounts
df1['num_bc_tl'].describe()
drawValCounts(df1['num_bc_tl'].value_counts(), 'num_bc_tl', 'vertical')

# Number of installment accounts
df1['num_il_tl'].describe()
drawValCounts(df1['num_il_tl'].value_counts(), 'num_il_tl', 'vertical')

# Number of open revolving accounts
df1['num_op_rev_tl'].describe()
drawValCounts(df1['num_op_rev_tl'].value_counts(), 'num_op_rev_tl', 'vertical')

# Number of revolving accounts
df1['num_rev_accts'].describe()
drawValCounts(df1['num_rev_accts'].value_counts(), 'num_rev_accts', 'vertical')

# Number of revolving accounts
df1['num_rev_tl_bal_gt_0'].describe()
drawValCounts(df1['num_rev_tl_bal_gt_0'].value_counts(), 'num_rev_tl_bal_gt_0', 'vertical')

# Number of satisfactory accounts
df1['num_sats'].describe()
drawValCounts(df1['num_sats'].value_counts(), 'num_sats', 'vertical')

# Number of accounts currently 120 days past due (updated in past 2 months)
df1['num_tl_120dpd_2m'].describe()
df1['num_tl_120dpd_2m'].value_counts()

# Number of accounts currently 30 days past due (updated in past 2 months)
df1['num_tl_30dpd'].value_counts()

# Number of accounts 90 or more days past due in last 24 months
df1['num_tl_90g_dpd_24m'].describe()
df1['num_tl_90g_dpd_24m'].value_counts()

# Number of accounts opened in past 12 months
df1['num_tl_op_past_12m'].describe()
df1['num_tl_op_past_12m'].value_counts()
drawValCounts(df1['num_tl_op_past_12m'].value_counts(), 'num_tl_op_past_12m', 'vertical')

# Percent of trades never delinquent
df1['pct_tl_nvr_dlq'].describe()
plt.hist(df1['pct_tl_nvr_dlq'], bins=20)

# Percentage of all bankcard accounts > 75% of limit.
df1['percent_bc_gt_75'].describe()
plt.hist(df1['percent_bc_gt_75'], bins=20)

# Number of public record bankruptcies
df1['pub_rec_bankruptcies'].describe()
drawValCounts(df1['pub_rec_bankruptcies'].value_counts(), 'pub_rec_bankruptcies', 'vertical')

# Number of tax liens
df1['tax_liens'].describe()

# Total high credit/credit limit
df1['tot_hi_cred_lim'].describe()
plt.hist(df1['tot_hi_cred_lim'], bins=20)

# Total credit balance excluding mortgage
df1['total_bal_ex_mort'].describe()
plt.hist(df1['total_bal_ex_mort'], bins=20)

# Total bankcard high credit/credit limit
df1['total_bc_limit'].describe()
plt.hist(df1['total_bc_limit'], bins=20)

# Total installment high credit/credit limit
df1['total_il_high_credit_limit'].describe()
plt.hist(df1['total_il_high_credit_limit'], bins=20)


df1['iBad'] = iBad
df1['iRent'], _ = pd.factorize(df1['home_ownership'] == 'RENT')
df1['iMort'], _ = pd.factorize(df1['home_ownership'] == 'MORTGAGE')
features = ['pub_rec_bankruptcies', 'revol_util2', 'inq_last_6mths', 'iRent', 'iMort', 'iBad']

X = df1[features].dropna()[features[:-1]]
y, _ = pd.factorize(df1[features].dropna()[features[-1]])

from scipy import interp
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold

mean_tpr = 0.0
mean_fpr = np.linspace(0, 1, 100)

cv = StratifiedKFold(n_splits=6)
colors = cycle(['cyan', 'indigo', 'seagreen', 'yellow', 'blue', 'darkorange'])
lw = 2
i = 0

for (train, test), color in zip(cv.split(X, y), colors):
    probas_ = clf.fit(X.iloc[train], y[train]).predict_proba(X.iloc[test])
    fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
    mean_tpr += interp(mean_fpr, fpr, tpr)
    mean_tpr[0] = 0.0
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, lw=lw, color=color, label='ROC fold %d (area = %0.2f)' % (i, roc_auc))
    i += 1

plt.plot([0, 1], [0, 1], linestyle='--', lw=lw, color='k', label='Luck')

mean_tpr /= cv.get_n_splits(X, y)
mean_tpr[-1] = 1.0
mean_auc = auc(mean_fpr, mean_tpr)
plt.plot(mean_fpr, mean_tpr, color='g', linestyle='--',
         label='Mean ROC (area = %0.2f)' % mean_auc, lw=lw)

plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()





import numpy as np
from scipy import interp
import matplotlib.pyplot as plt
from itertools import cycle

from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold

# import some data to play with
iris = datasets.load_iris()
X = iris.data
y = iris.target
X, y = X[y != 2], y[y != 2]
n_samples, n_features = X.shape

# Add noisy features
random_state = np.random.RandomState(0)
X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]

# Run classifier with cross-validation and plot ROC curves
cv = StratifiedKFold(n_splits=6)
classifier = svm.SVC(kernel='linear', probability=True,
                     random_state=random_state)

mean_tpr = 0.0
mean_fpr = np.linspace(0, 1, 100)

colors = cycle(['cyan', 'indigo', 'seagreen', 'yellow', 'blue', 'darkorange'])
lw = 2

i = 0
for (train, test), color in zip(cv.split(X, y), colors):
    probas_ = classifier.fit(X[train], y[train]).predict_proba(X[test])
    # Compute ROC curve and area the curve
    fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
    mean_tpr += interp(mean_fpr, fpr, tpr)
    mean_tpr[0] = 0.0
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, lw=lw, color=color,
             label='ROC fold %d (area = %0.2f)' % (i, roc_auc))

    i += 1

plt.plot([0, 1], [0, 1], linestyle='--', lw=lw, color='k',
         label='Luck')

mean_tpr /= cv.get_n_splits(X, y)
mean_tpr[-1] = 1.0
mean_auc = auc(mean_fpr, mean_tpr)
plt.plot(mean_fpr, mean_tpr, color='g', linestyle='--',
         label='Mean ROC (area = %0.2f)' % mean_auc, lw=lw)

plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
