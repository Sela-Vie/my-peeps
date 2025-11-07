# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: testing for the routes and endpoints
# ========================================================================
# HEADERS
# ========================================================================

import requests as req

# ========================================================================

url:str = "http://127.0.0.1:5000/"

# request:req.Response = req.get(
# 	url=url + "people/birthdays",
# 	timeout=2,
#     json = {
#         "month" : 8
#     }
# )
# for stuff in request.json():
#     print(stuff)
# print("\n\n")

# request:req.Response = req.get(
# 	url=url + "people/birthdays",
# 	timeout=2
# )
# for stuff in request.json():
#     print(stuff)
# print("\n\n")

# ========================================================================

# for j in range(1, 13):
# 	for i in range(1, 3):
# 		request:req.Response = req.post(
# 			url=url + "people",
# 			timeout=2,
# 			json = {
# 				"name_first" : "Jhon", 
# 				"name_last" : f"Doe_{j}",
# 				"birth_date" : f"{i}",
# 				"birth_month" : f"{j}",
# 				"birth_year" : f"{i}"
# 			}
# 		)
# 		print(request.json())
# print("\n\n")

# ========================================================================


request:req.Response = req.put(
	url=url + "people",
	timeout=2,
	json = {
		"id" : 24,
		"name_first" : "kill", 
		"name_last" : "me",
		"birth_date" : 5,
		"birth_month" : 12,
		"birth_year" : 2002
	}
)
print(request.text)
print("\n\n")

request:req.Response = req.delete(
	url=url + "people",
	timeout=2,
	json = {
		"id" : 23
	}
)
print(request.text)
print("\n\n")


request:req.Response = req.get(
	url=url + "people",
	timeout=2
)
for stuff in request.json():
	print(stuff)
print("\n\n")

