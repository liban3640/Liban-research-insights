import statsmodels.api as sm
from statsmodels.formula.api import ols

# Example - assuming 'Writing Proficiency Level' across different groups (e.g., groups of students)
# model = ols('Writing Proficiency Level ~ C(Group)', data=df).fit()
# anova_table = sm.stats.anova_lm(model, typ=2)

# print(anova_table)