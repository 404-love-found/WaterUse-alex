# Run 2 — meta-llama/Llama-3.3-70B-Instruct-Turbo

Here are the distinct action situations extracted from the model using the IAD framework:

1. **Capacitor Adoption Game**
	* Title: Capacitor Adoption Game
	* Location: Transformer group level
	* Players: Farmer, Neighbor Farmer
	* Roles: Electricity consumer, Peer
	* Actions: Adopt capacitor, Do not adopt capacitor
	* Control Rules: Adoption leads to improved voltage quality, but only if multiple farmers adopt
	* Information: Past voltage quality, peer adoption rates
	* Outcomes: Improved voltage quality, increased adoption costs
	* Payoffs: 
		|  | Adopt Capacitor | Do not Adopt Capacitor |
		| --- | --- | --- |
		| Adopt Capacitor | 3, 3 | 1, 2 |
		| Do not Adopt Capacitor | 2, 1 | 0, 0 |
	* Strategic Tension: Coordination game, where farmers need to coordinate adoption decisions to achieve improved voltage quality
	* Temporal Structure: Repeated annually
	* Relevant Rules: Boundary rules define the transformer group, choice rules specify adoption decisions

2. **Groundwater Extraction Game**
	* Title: Groundwater Extraction Game
	* Location: Aquifer level
	* Players: Farmer, Neighbor Farmer
	* Roles: Groundwater extractor, Peer
	* Actions: Extract groundwater, Restrain extraction
	* Control Rules: Extraction leads to decreased aquifer levels, increased pumping costs
	* Information: Past extraction rates, aquifer levels
	* Outcomes: Decreased aquifer levels, increased pumping costs
	* Payoffs: 
		|  | Extract Groundwater | Restrain Extraction |
		| --- | --- | --- |
		| Extract Groundwater | 2, 2 | 3, 1 |
		| Restrain Extraction | 1, 3 | 0, 0 |
	* Strategic Tension: Common pool resource game, where farmers need to balance individual extraction decisions with collective sustainability
	* Temporal Structure: Continuous over time
	* Relevant Rules: Boundary rules define the aquifer, choice rules specify extraction decisions

3. **Authorization Game**
	* Title: Authorization Game
	* Location: Substation level
	* Players: Farmer, Substation Staff
	* Roles: Electricity consumer, Service provider
	* Actions: Seek authorization, Do not seek authorization
	* Control Rules: Authorization leads to formal connection, increased costs
	* Information: Past authorization rates, connection costs
	* Outcomes: Formal connection, increased costs
	* Payoffs: 
		|  | Seek Authorization | Do not Seek Authorization |
		| --- | --- | --- |
		| Seek Authorization | 2, 3 | 1, 2 |
		| Do not Seek Authorization | 3, 1 | 0, 0 |
	* Strategic Tension: Game of trust, where farmers need to trust substation staff to provide reliable service
	* Temporal Structure: One-shot
	* Relevant Rules: Boundary rules define the substation, choice rules specify authorization decisions

4. **Collusion Exchange Game**
	* Title: Collusion Exchange Game
	* Location: Substation level
	* Players: Farmer, Substation Staff
	* Roles: Electricity consumer, Service provider
	* Actions: Offer informal exchange, Do not offer informal exchange
	* Control Rules: Informal exchange leads to reciprocal benefits, increased risk of detection
	* Information: Past exchange rates, detection risk
	* Outcomes: Reciprocal benefits, increased risk of detection
	* Payoffs: 
		|  | Offer Informal Exchange | Do not Offer Informal Exchange |
		| --- | --- | --- |
		| Offer Informal Exchange | 3, 3 | 1, 2 |
		| Do not Offer Informal Exchange | 2, 1 | 0, 0 |
	* Strategic Tension: Game of trust, where farmers and substation staff need to trust each other to maintain informal exchange
	* Temporal Structure: Repeated annually
	* Relevant Rules: Boundary rules define the substation, choice rules specify exchange decisions

5. **Capacity Provision Game**
	* Title: Capacity Provision Game
	* Location: Transformer group level
	* Players: Farmer, Substation Staff
	* Roles: Electricity consumer, Service provider
	* Actions: Contribute to capacity, Do not contribute to capacity
	* Control Rules: Contribution leads to improved transformer capacity, increased costs
	* Information: Past contribution rates, capacity levels
	* Outcomes: Improved transformer capacity, increased costs
	* Payoffs: 
		|  | Contribute to Capacity | Do not Contribute to Capacity |
		| --- | --- | --- |
		| Contribute to Capacity | 2, 3 | 1, 2 |
		| Do not Contribute to Capacity | 3, 1 | 0, 0 |
	* Strategic Tension: Public goods game, where farmers need to contribute to shared capacity to achieve improved reliability
	* Temporal Structure: Repeated annually
	* Relevant Rules: Boundary rules define the transformer group, choice rules specify contribution decisions

6. **Social Learning Game**
	* Title: Social Learning Game
	* Location: Village level
	* Players: Farmer, Neighbor Farmer
	* Roles: Electricity consumer, Peer
	* Actions: Observe neighbor adoption, Do not observe neighbor adoption
	* Control Rules: Observation leads to updated adoption decisions
	* Information: Past adoption rates, neighbor adoption decisions
	* Outcomes: Updated adoption decisions
	* Payoffs: Not applicable (non-strategic sequential process)
	* Strategic Tension: Not applicable (non-strategic sequential process)
	* Temporal Structure: Continuous over time
	* Relevant Rules: Boundary rules define the village, choice rules specify observation decisions

Each game represents a distinct strategic tension with ordinal payoffs grounded in the electricity-irrigation governance context. The payoffs reflect the likely consequences of each combined action, and the games are designed to ensure strategic diversity.