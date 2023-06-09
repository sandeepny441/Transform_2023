# value counts 
s.value_counts()  
s.unique()
s.nunique()

# missing data 
s.isnull().sum()
s.dropna()
s.fillna(value)

# apply functions 
s.apply(func)
s.map(dict)

# sorting 
s.sort_values()
s.sort_index()

#data allignment 
s.reindex()
s.reset_index()

#membership 
s.isin(values)

# more 
s.astype(dtype) # Cast values to dtype
s.replace(val1, val2) # Replace values 
s.rename() # Rename index labels
s.between(val1, val2) # Filter between values
s.duplicated() # Check for duplicates
s.interpolate() # Fill NaNs by interpolation 
s.clip(lower, upper) # Trim values to range
s.expanding(min_periods).mean() # Expanding statistics
