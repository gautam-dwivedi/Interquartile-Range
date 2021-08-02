
## Import Libraries
import numpy as np
import pandas as pd
def main():
	Dataset = [7,7,47,87,31,75,177,119,31,115,155,119,116]
	print(Dataset)
	print(sorted(Dataset))
	
	quantile1, quantile3 = np.percentile(Dataset,[25,75])
	print("Quantile values are:", quantile1,quantile3)
	
	## Find the IQR

	iqr_value = quantile3-quantile1
	print("IQR is:",iqr_value)
	
	
	## Find the lower bound value and the higher bound value

	lower_bound_val = quantile1 -(1.5 * iqr_value) 
	upper_bound_val = quantile3 +(1.5 * iqr_value)

	print(lower_bound_val,upper_bound_val)
	
	print("Values Below lower and above upper bound values are outliers")
	
if __name__ == "__main__":
	main()