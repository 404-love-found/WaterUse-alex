# Run 11 — meta-llama/Llama-3.3-70B-Instruct-Turbo

Here are the distinct action situations extracted from the model using the IAD framework:

1. **Capacity Provision Game**
	* Title: Capacity Provision Game
	* Location: Transformer group level
	* Players: Farmers, Substation staff
	* Roles: Electricity consumers, Service providers
	* Actions: Farmers - Invest in transformer capacity, Free-ride; Substation staff - Invest in service delivery, Deny service
	* Control Rules: Farmers' investment decisions affect transformer capacity, which in turn affects electricity quality and reliability
	* Information: Farmers have partial information about their neighbors' investment decisions; Substation staff have complete information about farmers' investment decisions
	* Outcomes: Transformer capacity, Electricity quality, Reliability
	* Payoffs: 
		|  | Invest | Free-ride |
		| --- | --- | --- |
		| Invest | 3, 2 | 1, 3 |
		| Deny service | 0, 1 | 2, 0 |
	* Strategic Tension: Public Goods Game - Farmers face a dilemma between contributing to shared transformer capacity and free-riding on their neighbors' investments
	* Temporal Structure: Repeated annually
	* Relevant Rules: Boundary rules - Farmers can invest in transformer capacity or free-ride; Choice rules - Substation staff can invest in service delivery or deny service

2. **Collusion Exchange Game**
	* Title: Collusion Exchange Game
	* Location: Substation level
	* Players: Farmers, Substation staff
	* Roles: Electricity consumers, Enforcers
	* Actions: Farmers - Offer bribe, Refuse to bribe; Substation staff - Accept bribe, Reject bribe
	* Control Rules: Farmers' bribe offers affect substation staff's enforcement decisions
	* Information: Farmers have partial information about substation staff's corruption levels; Substation staff have complete information about farmers' bribe offers
	* Outcomes: Enforcement level, Bribe payment
	* Payoffs: 
		|  | Offer bribe | Refuse to bribe |
		| --- | --- | --- |
		| Accept bribe | 3, 2 | 0, 1 |
		| Reject bribe | 1, 3 | 2, 0 |
	* Strategic Tension: Game of Trust - Farmers face a dilemma between offering a bribe to substation staff and risking rejection or refusing to bribe and risking enforcement
	* Temporal Structure: Repeated annually
	* Relevant Rules: Boundary rules - Farmers can offer a bribe or refuse to bribe; Choice rules - Substation staff can accept a bribe or reject a bribe

3. **Groundwater Extraction Game**
	* Title: Groundwater Extraction Game
	* Location: Aquifer level
	* Players: Farmers
	* Roles: Groundwater extractors
	* Actions: Extract water, Restrain extraction
	* Control Rules: Farmers' extraction decisions affect aquifer level and pumping costs
	* Information: Farmers have partial information about their neighbors' extraction decisions
	* Outcomes: Aquifer level, Pumping costs
	* Payoffs: 
		|  | Extract | Restrain |
		| --- | --- | --- |
		| Extract | 2, 2 | 0, 3 |
		| Restrain | 3, 0 | 1, 1 |
	* Strategic Tension: Common Pool Resource Game - Farmers face a dilemma between extracting groundwater and risking over-extraction or restraining extraction and risking lost benefits
	* Temporal Structure: Continuous over time
	* Relevant Rules: Boundary rules - Farmers can extract water or restrain extraction; Choice rules - Farmers can choose their extraction levels

4. **Authorization Game**
	* Title: Authorization Game
	* Location: Substation level
	* Players: Farmers, Substation staff
	* Roles: Electricity consumers, Service providers
	* Actions: Farmers - Seek formal connection, Seek informal connection; Substation staff - Invest in service delivery, Deny service
	* Control Rules: Farmers' connection decisions affect substation staff's investment decisions
	* Information: Farmers have partial information about substation staff's investment decisions; Substation staff have complete information about farmers' connection decisions
	* Outcomes: Connection type, Service quality
	* Payoffs: 
		|  | Formal connection | Informal connection |
		| --- | --- | --- |
		| Invest in service | 3, 2 | 1, 3 |
		| Deny service | 0, 1 | 2, 0 |
	* Strategic Tension: Authorization Game - Farmers face a dilemma between seeking a formal connection and risking denial or seeking an informal connection and risking low service quality
	* Temporal Structure: Repeated annually
	* Relevant Rules: Boundary rules - Farmers can seek a formal or informal connection; Choice rules - Substation staff can invest in service delivery or deny service

5. **DSM Coordination Game**
	* Title: DSM Coordination Game
	* Location: Transformer group level
	* Players: Farmers
	* Roles: Electricity consumers
	* Actions: Adopt DSM technology, Refuse to adopt
	* Control Rules: Farmers' adoption decisions affect transformer capacity and electricity quality
	* Information: Farmers have partial information about their neighbors' adoption decisions
	* Outcomes: Transformer capacity, Electricity quality
	* Payoffs: 
		|  | Adopt | Refuse to adopt |
		| --- | --- | --- |
		| Adopt | 3, 3 | 0, 2 |
		| Refuse to adopt | 2, 0 | 1, 1 |
	* Strategic Tension: Coordination Game - Farmers face a dilemma between adopting DSM technology and risking low adoption rates or refusing to adopt and risking low electricity quality
	* Temporal Structure: Repeated annually
	* Relevant Rules: Boundary rules - Farmers can adopt DSM technology or refuse to adopt; Choice rules - Farmers can choose their adoption levels

6. **Social Learning Game**
	* Title: Social Learning Game
	* Location: Village level
	* Players: Farmers
	* Roles: Electricity consumers
	* Actions: Observe neighbors, Adopt DSM technology
	* Control Rules: Farmers' observation decisions affect their adoption decisions
	* Information: Farmers have partial information about their neighbors' adoption decisions
	* Outcomes: Adoption rate, Electricity quality
	* Payoffs: Not applicable (non-strategic sequential process)
	* Strategic Tension: Not applicable (non-strategic sequential process)
	* Temporal Structure: Continuous over time
	* Relevant Rules: Boundary rules - Farmers can observe their neighbors or not; Choice rules - Farmers can choose to adopt DSM technology or not

Each game complies with the ODD+D description, and the payoff matrices reflect the strategic tensions and incentive structures described in the model. The games are distinct and capture different governance interactions, including public goods, trust, common pool resources, authorization, coordination, and social learning.