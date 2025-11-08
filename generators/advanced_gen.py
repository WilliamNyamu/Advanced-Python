import statistics
# finding the sum total of funds raised in series a
filename = "C:/Users/Billy/Downloads/techcrunch.csv"
# lines = (line for line in open(filename))
# list_line = (s.rstrip().split(",") for s in lines)
# cols = next(list_line)
# company_dicts = (dict(zip(cols, data)) for data in list_line)
# funding = (
#     int(company_dict["raisedAmt"])
#     for company_dict in company_dicts
#     if company_dict["round"] == "a"
# )
# total_series_a = sum(funding)
# print(f"Total series A fundraising: ${total_series_a}")

lines = (line for line in open(filename))
lines_split = (s.rstrip().split(',') for s in lines)
cols = next(lines_split)
company_dicts = (dict(zip(cols, data)) for data in lines_split)
avg_funding = (int(company_dict['raisedAmt'])  for company_dict in company_dicts if company_dict['round'] == 'a')
total_avg = statistics.mean(avg_funding)
print(f"Total Average Amount for Series A fundraising: ${total_avg}")
