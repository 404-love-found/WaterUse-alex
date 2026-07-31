# Run 8 — meta-llama/Llama-3.3-70B-Instruct-Turbo

### 1. Capacitor Adoption Game
- **Title**: Capacitor Adoption
- **Location**: Transformer group level
- **Players**: Farmers
- **Roles**: Electricity consumers
- **Actions**: Invest in capacitor, Do not invest
- **Control Rules**: Collective adoption leads to shared benefits
- **Information**: Past voltage quality, peer adoption rates
- **Outcomes**: Budget change, grid quality change
- **Payoffs**: 
  |  | Invest | Do not invest |
  | --- | --- | --- |
  | **Invest** | 3, 3 | 0, 2 |
  | **Do not invest** | 2, 0 | 1, 1 |
- **Strategic Tension**: Coordination game, similar to the **DSM Coordination Game**. Farmers must decide whether to invest in capacitors, with the benefit depending on how many neighbors also adopt.
- **Temporal Structure**: Repeated annually
- **Relevant Rules**: Collective adoption threshold, budget constraints

### 2. Groundwater Extraction Game
- **Title**: Groundwater Extraction
- **Location**: Aquifer level
- **Players**: Farmers
- **Roles**: Water extractors
- **Actions**: Extract at full rate, Restrain extraction
- **Control Rules**: Aquifer depletion increases pumping costs
- **Information**: Current aquifer level, extraction costs
- **Outcomes**: Aquifer level change, pumping cost change
- **Payoffs**: 
  |  | Extract | Restrain |
  | --- | --- | --- |
  | **Extract** | 2, 2 | 3, 0 |
  | **Restrain** | 0, 3 | 1, 1 |
- **Strategic Tension**: Common Pool Resource game, similar to the **Common Pool Resource Game**. Farmers must balance individual extraction benefits with collective sustainability.
- **Temporal Structure**: Continuous over time
- **Relevant Rules**: Aquifer depletion rate, pumping cost function

### 3. Collusion Exchange Game
- **Title**: Collusion Exchange
- **Location**: Substation level
- **Players**: Farmer, Substation staff
- **Roles**: Service seeker, Service provider
- **Actions**: Offer bribe, Accept bribe
- **Control Rules**: Bribe acceptance leads to informal connection
- **Information**: Discretionary power, collusion network density
- **Outcomes**: Connection status change, budget change
- **Payoffs**: 
  |  | Offer bribe | Do not offer bribe |
  | --- | --- | --- |
  | **Accept bribe** | 3, 3 | 0, 2 |
  | **Do not accept bribe** | 2, 0 | 1, 1 |
- **Strategic Tension**: **Collusion Exchange Game**. Farmers and staff engage in informal exchanges, with outcomes depending on mutual willingness and detection risk.
- **Temporal Structure**: Repeated annually
- **Relevant Rules**: Discretionary power, collusion network effects

### 4. Authorization Game
- **Title**: Authorization
- **Location**: Substation level
- **Players**: Farmer, Substation staff
- **Roles**: Service seeker, Service provider
- **Actions**: Seek formal connection, Invest in formal connection
- **Control Rules**: Formal connection leads to reliable service
- **Information**: Connection costs, service reliability
- **Outcomes**: Connection status change, budget change
- **Payoffs**: 
  |  | Seek connection | Do not seek connection |
  | --- | --- | --- |
  | **Invest in connection** | 3, 3 | 0, 2 |
  | **Do not invest** | 2, 0 | 1, 1 |
- **Strategic Tension**: **Authorization Game**. Farmers decide whether to seek formal connections, while staff decide whether to invest in service delivery.
- **Temporal Structure**: Repeated annually
- **Relevant Rules**: Connection costs, service reliability function

### 5. Capacity Provision Game
- **Title**: Capacity Provision
- **Location**: Transformer group level
- **Players**: Farmers
- **Roles**: Electricity consumers
- **Actions**: Contribute to capacity, Free-ride
- **Control Rules**: Collective contribution leads to shared capacity
- **Information**: Current capacity, peer contribution rates
- **Outcomes**: Capacity change, budget change
- **Payoffs**: 
  |  | Contribute | Free-ride |
  | --- | --- | --- |
  | **Contribute** | 3, 3 | 0, 2 |
  | **Free-ride** | 2, 0 | 1, 1 |
- **Strategic Tension**: **Public Goods Game**. Farmers must decide whether to contribute to shared electrical infrastructure capacity.
- **Temporal Structure**: Repeated annually
- **Relevant Rules**: Capacity contribution threshold, budget constraints

### 6. Social Learning Game
- **Title**: Social Learning
- **Location**: Village level
- **Players**: Farmers
- **Roles**: Observers
- **Actions**: Observe, Imitate
- **Control Rules**: Observations influence adoption decisions
- **Information**: Neighbor adoption rates, outcomes
- **Outcomes**: Adoption rate change
- **Payoffs**: 
  |  | Observe | Imitate |
  | --- | --- | --- |
  | **Observe** | 1, 1 | 2, 3 |
  | **Imitate** | 3, 2 | 0, 1 |
- **Strategic Tension**: Non-strategic sequential process, similar to the **Social Learning Game**. Farmers observe and imitate their neighbors' adoption decisions.
- **Temporal Structure**: Continuous over time
- **Relevant Rules**: Observation and imitation mechanisms

Each game represents a distinct strategic tension or non-strategic sequential process, with payoffs grounded in the electricity-irrigation governance context. The games comply with the ODD+D description, capturing the complexities of decentralized electricity-irrigation settings, including institutional asymmetries, environmental feedback, and social learning.