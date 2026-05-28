import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const root = "/Users/alex-lirio-lucian/develop/WaterUse-alex/LLM_Prompting";
const sourcePath = path.join(root, "ODD_electricity", "Electricity_ODD.xlsx");
const outputPath = path.join(root, "ODD_EV-parking", "ODD_EV-parking.xlsx");

const answers = [
  ["Apartment EV parking case study (original)"],
  ["\u00a0"],
  ["\u00a0"],
  [
    "To understand how fair queue access emerges or breaks down in an apartment parking facility with limited shared EV chargers, discounted per-kWh charging for residents, regular per-kWh charging for non-residents, and mixed resident/visitor demand.",
  ],
  [
    "For researchers, building managers, mobility planners, and policymakers interested in shared EV-charging governance, queue fairness, apartment amenity management, and access to scarce urban charging infrastructure.",
  ],
  ["\u00a0"],
  ["Human agents: apartment residents with EVs, non-resident EV users, parking-lot management staff, and building management."],
  ["Institutional entities: resident discount rules, posted queue rules, reservation procedures, complaint channels, and enforcement policies."],
  ["Physical and digital entities: charging points, charging bays, non-charging parking bays, local garage electrical capacity, and the queue or reservation platform."],
  [
    "Residents: residency status, discount eligibility, battery state of charge, desired kWh, schedule flexibility, queue position, reservation status, wait time, willingness to move promptly, past charging experience, perceived fairness, and social ties with staff or neighbours.",
  ],
  [
    "Non-resident users: visitor/public-parking status, regular per-kWh price, desired kWh, battery urgency, time flexibility, queue position, wait time, willingness to comply, and perceived legitimacy of using apartment chargers.",
  ],
  [
    "Parking staff and management: enforcement effort, ability to verify resident status, ability to monitor occupied chargers, complaint backlog, maintenance coordination, tolerance of exceptions, and reputation concerns.",
  ],
  [
    "Chargers and queue system: number of plugs, charging rate, operational status, occupied-but-not-charging status, fault state, repair delay, reservation windows, waiting order, no-shows, and recorded violations.",
  ],
  [
    "EV arrival demand, household routines, commuting schedules, visitor demand, local events, weather, base electricity prices, building occupancy, charger hardware reliability, external utility interruptions, and public parking demand.",
  ],
  [
    "Space is represented through one apartment parking facility. Chargers are located in a limited number of charging bays, while most parking spaces cannot charge vehicles. Resident access points, visitor entrances, staff offices, and charger visibility affect monitoring and queue behaviour.",
  ],
  [
    "Temporal: 15-minute intervals within daily charging cycles; monthly billing and complaint summaries.",
  ],
  [
    "Spatial: one apartment garage with shared resident and non-resident access, a small number of charging bays, and a larger set of ordinary parking bays.",
  ],
  ["\u00a0"],
  [
    "1. At the beginning of a day, EV users estimate energy need, charger availability, likely wait time, and whether queue rules will be enforced.",
  ],
  [
    "2. Users decide whether to reserve a slot, join the live queue, arrive without reservation, charge during off-peak periods, request informal priority, or leave for another charger.",
  ],
  [
    "3. The queue platform updates waiting order, reservation status, charger availability, user category, no-shows, and completed sessions.",
  ],
  [
    "4. Parking staff observe some violations and complaints, then decide whether to preserve queue order, ask overstaying vehicles to move, cancel no-shows, tolerate exceptions, or request maintenance.",
  ],
  ["\u00a0"],
  ["\u00a0"],
  [
    "The model draws on shared infrastructure governance, queue fairness, congestion in limited-capacity facilities, bounded rationality, rule compliance, institutional trust, and social learning. The central complexity comes from interdependent decisions: one user's arrival time, queue behaviour, charging duration, and move-out decision affect the next user's access.",
  ],
  [
    "Agents are boundedly rational. Users do not know exact future arrivals, charger failures, no-shows, or enforcement response. They rely on app signals, visible queue length, past waiting times, and perceived fairness.",
  ],
  [
    "Rule-based and heuristic decision models are chosen because apartment charging behaviour depends on routines, experience, visible enforcement, complaint outcomes, and local norms rather than complete optimisation.",
  ],
  [
    "The model can be parameterised from charger-session logs, queue-app records, resident eligibility records, apartment parking records, complaint logs, maintenance tickets, surveys, and electricity-meter data.",
  ],
  ["Charging-session level, user-category level, charger level, day level, and monthly billing level."],
  ["\u00a0"],
  [
    "EV users decide when to seek charging, whether to reserve, whether to join or bypass a queue, how much energy to request, whether to move promptly after useful charging, whether to complain about violations, and whether to search for another charger. Parking staff decide whether to enforce queue order, verify resident status, respond to complaints, remove overstaying vehicles, grant exceptions, and request maintenance.",
  ],
  [
    "Users seek enough energy for expected travel while minimizing waiting, uncertainty, walking distance, conflict, and charging cost. Residents value discounted access to an apartment amenity. Non-residents value predictable access once admitted to the parking facility. Management seeks low complaint volume, high charger utilisation, resident satisfaction, visitor revenue, and manageable enforcement effort.",
  ],
  [
    "Users compare expected wait time, battery urgency, resident discount status, visible charger occupancy, past enforcement, and perceived legitimacy of the queue. If rule-following produced reliable access in the past, users are more likely to follow the queue. If bypassing or overstaying was tolerated, some users become more likely to attempt similar behaviour.",
  ],
  [
    "Yes. Users adapt to queue length, time of day, charger faults, resident/non-resident access shares, and visible enforcement. Staff adapt to complaint volume, repeated violations, charger downtime, and resident pressure.",
  ],
  [
    "Yes. Norms of neighbourly fairness, resident entitlement, equal treatment for admitted users, first-come-first-served order, and reciprocity with staff shape behaviour. Informal relationships can support orderly use or undermine queue fairness.",
  ],
  ["Yes. Charger-bay location, distance from apartment elevators, visitor entrances, and staff offices affects convenience, visibility, and enforcement."],
  ["Yes. Morning departures, evening returns, overnight charging, reservation windows, charging completion notifications, and monthly billing cycles shape decisions."],
  [
    "Uncertainty enters through unknown future arrivals, charger faults, no-shows, charging completion times, staff response, and whether other users will move promptly. Users estimate these conditions from past experience and platform signals.",
  ],
  ["\u00a0"],
  ["Yes, through experience with waiting, successful charging attempts, observed violations, and staff responses. Users update their expectations about whether off-peak reservation, queue compliance, complaint filing, or opportunistic behaviour is likely to work."],
  ["Collective learning is represented implicitly through shared expectations that emerge when many users observe the same enforcement pattern or queue outcome."],
  ["\u00a0"],
  [
    "Users sense queue length, app-estimated wait time, charger status, occupied bays, charging completion notices, price category, past charging success, and whether staff intervene. Sensing is imperfect because drivers may not know whether a vehicle is still charging, waiting for its owner, blocked by a fault, or deliberately overstaying.",
  ],
  [
    "Users can observe visible charger occupation, queue movement, resident or visitor signage in some cases, and whether another driver bypasses the queue. They cannot perfectly observe another user's battery need, reservation legitimacy, or private communication with staff.",
  ],
  ["Local garage scale and digital platform scale."],
  ["Information comes from the queue app, charger interface, posted rules, physical observation, staff messages, and complaint outcomes."],
  ["Cognitive and information-gathering costs are not monetised, but checking the app, walking to the charger area, and contacting staff can affect choices."],
  ["\u00a0"],
  ["Users use past wait times, time of day, day of week, queue-app estimates, visible charger status, and memory of enforcement. Staff use complaints, charger logs, violation history, and maintenance records."],
  ["Users rely on heuristics such as evenings are crowded, resident users are more likely to use the chargers, off-peak reservations often work, staff rarely intervene, or queue skipping is risky when complaints are high."],
  [
    "Yes. Users may overestimate resident priority, underestimate visitor demand, misread charger availability, or assume that past lax enforcement will continue. Staff may underestimate the fairness cost of small queue violations.",
  ],
  ["\u00a0"],
  [
    "Both. Users interact indirectly through queue order, charging duration, bay occupation, and move-out timing. They may interact directly when contesting queue order or asking a driver to move. Users interact with staff through complaints, verification, and informal requests.",
  ],
  ["Interactions depend on user category, queue position, charging urgency, visible occupancy, staff monitoring, past enforcement, resident discount policy, and charger reliability."],
  ["Communication is represented through app notifications, complaint tickets, staff messages, posted rules, informal conversations, and visible behaviour in the garage."],
  [
    "Resident networks, building communication channels, and informal staff-user relationships can influence whether users follow off-peak charging norms, tolerate queue order, or seek preferential treatment. These networks emerge from repeated use and apartment life rather than being imposed.",
  ],
  ["\u00a0"],
  [
    "Yes. Users belong to resident and non-resident categories. Residents may also belong to neighbour networks or building communication groups. These groups affect discount eligibility, perceived entitlement, information sharing, and pressure on management.",
  ],
  ["Collectives are represented through user category, social ties, shared information, complaint pressure, and group-level access outcomes."],
  ["\u00a0"],
  [
    "Yes. Users differ in resident status, battery size, urgency, work schedule, willingness to wait, discount eligibility, flexibility, past charging experience, social ties, and sensitivity to fairness. Staff differ in enforcement effort and tolerance for exceptions.",
  ],
  [
    "Yes. Some users comply with posted rules even when enforcement is weak. Others react strongly to delays or use informal strategies. Residents and non-residents may interpret the same queue rule differently because residents receive a price discount.",
  ],
  ["\u00a0"],
  ["EV arrivals, desired kWh, session duration, no-shows, charger faults, repair delays, staff observation of violations, and unexpected visitor demand are random or partly random."],
  ["\u00a0"],
  [
    "Average wait time, queue length, completed sessions, resident/non-resident access share, kWh delivered, charger utilisation, overstay duration, queue violations, complaints, enforcement actions, and charger downtime are collected daily and monthly.",
  ],
  [
    "Stable or unstable queue fairness, resident dominance of charger access, visitor displacement, off-peak charging norms, informal priority patterns, chronic overstaying, complaint cascades, and changing trust in the charging system can emerge.",
  ],
  ["\u00a0"],
  ["\u00a0"],
  ["The model can be implemented as a discrete-time ABM with 15-minute steps. EV users and parking staff are agents; chargers, charging bays, and the queue platform are shared infrastructure states."],
  ["Can be made available upon request."],
  ["\u00a0"],
  [
    "The apartment parking facility starts with a fixed number of charging bays, a larger number of EV users than chargers, posted queue rules, resident discount eligibility, regular visitor pricing, a queue or reservation platform, and initial charger reliability conditions.",
  ],
  ["Initialisation can vary by number of chargers, resident EV adoption rate, non-resident demand, enforcement strength, charger reliability, queue-rule strictness, and size of the resident discount."],
  ["Initial values can be based on apartment occupancy, EV ownership estimates, charger-session records, parking access data, complaint logs, and observed charging demand."],
  ["\u00a0"],
  [
    "The model can use arrival schedules, charger reliability estimates, electricity prices, resident eligibility records, historical charging-session data, complaint records, and maintenance logs. It can also run with synthetic demand scenarios.",
  ],
  ["\u00a0"],
  [
    "Driver arrival and energy demand: users arrive according to resident routines, visitor demand, time of day, and battery urgency. Desired energy is measured in kWh. Queue formation and reservation: users can reserve a slot, join a live queue, or arrive without reservation; the platform orders users by posted rules and records no-shows. Charging session: a charger delivers energy until the user's requested amount is met, the user stops charging, or the session is interrupted by a fault. Bay release: a vehicle may leave promptly after useful charging or remain in the charging bay, blocking the next user even when little energy is delivered. Rule enforcement: staff observe some violations and decide whether to preserve queue order, ask overstaying users to move, cancel no-shows, tolerate exceptions, or respond to complaints. Discount billing: all users pay by kWh; residents pay a discounted rate, while non-residents pay the regular rate. Maintenance and reliability: faults reduce effective capacity until staff or technicians respond. Capacity planning: management evaluates whether to add chargers, improve monitoring, or revise rules based on demand, complaints, utilisation, and resident pressure.",
  ],
  [
    "Parameters include number of charging bays, resident discount rate, regular per-kWh price, arrival rate, desired-kWh distribution, charging speed, overstay tolerance, queue-rule compliance probability, staff monitoring probability, complaint response threshold, no-show rate, fault probability, repair delay, and resident/non-resident demand ratio.",
  ],
  [
    "Submodels are designed to represent shared charging access: demand formation, queue ordering, charging duration, bay release, rule enforcement, complaint feedback, maintenance, and capacity stress. Parameters can be calibrated from apartment garage operations or varied systematically for scenario analysis.",
  ],
];

if (answers.length !== 81) {
  throw new Error(`Expected 81 answer rows, got ${answers.length}`);
}

const source = await FileBlob.load(sourcePath);
const workbook = await SpreadsheetFile.importXlsx(source);
const sheet = workbook.worksheets.getItem("Sheet1");
const expectedAs = workbook.worksheets.add("Expected AS");

sheet.getRange("B1:B81").values = answers;
sheet.getRange("C1:D81").values = Array.from({ length: 81 }, () => [null, null]);

const expectedAsRows = [
  ["Expected action situations for EV parking evaluation", null, null, null, null],
  ["Use Sheet1 as the model input. This sheet is the hidden evaluation reference and should not be included in model prompts.", null, null, null, null],
  [null, null, null, null, null],
  ["AS ID", "Correct AS title", "Players", "Core choices", "Why it is correct"],
  [
    "AS1",
    "Queue-order and prompt move-out compliance between EV users",
    "Two EV users competing for scarce charger access, including residents and non-residents.",
    "Follow posted queue and move promptly after useful charging; or bypass the queue, claim a bay out of order, or remain after useful charging.",
    "This captures the direct fairness problem in a shared queue: individual shortcutting can improve one user's access while making waiting less reliable for others.",
  ],
  [
    "AS2",
    "Sequential learning in reservation and off-peak charging behaviour",
    "An early EV user whose behaviour is observed, and a later EV user who updates behaviour from that observation.",
    "Use a rule-aligned reservation/off-peak strategy or opportunistic behaviour; later users imitate or continue prior behaviour.",
    "This captures repeated learning: visible success can spread cooperative off-peak use, while visible opportunism can spread queue violations.",
  ],
  [
    "AS3",
    "Shared charger-capacity contribution dilemma among residents",
    "Residents who can support or oppose paying for more chargers, better monitoring, or rule improvements.",
    "Contribute to capacity or governance improvement; or wait and rely on others to bear the cost.",
    "This captures a contribution dilemma for shared apartment infrastructure: everyone benefits from improved capacity, but each resident may prefer others to pay first.",
  ],
  [
    "AS4",
    "Informal priority exchange between EV user and parking staff",
    "An EV user and a parking staff member who can influence access to a charging bay.",
    "Use the official queue or request informal priority; enforce posted order or grant informal priority.",
    "This captures how informal exceptions can benefit immediate parties while damaging the legitimacy of the official queue.",
  ],
  [
    "AS5",
    "Formal complaint and enforcement coordination between user and management",
    "A waiting EV user and apartment or parking management.",
    "Report unfair access, overstay, or malfunction; or stay silent. Management responds/enforces/repairs or delays.",
    "This captures institutional coordination: fair access improves when users report problems and management responds, but trust falls when either side withholds effort.",
  ],
  [
    "AS6",
    "Shared charger-occupancy common-pool congestion between EV users",
    "EV users drawing from the same limited charger-bay capacity.",
    "Use only needed kWh and release promptly; or maximize the session by taking more kWh, staying plugged in, or occupying the bay longer.",
    "This captures the common-pool congestion created when all users pay only by kWh and bay occupation time is not separately priced.",
  ],
];

expectedAs.getRange("A1:E10").values = expectedAsRows;
expectedAs.getRange("A1:E1").format.font.bold = true;
expectedAs.getRange("A1:E1").format.fill.color = "#D9EAF7";
expectedAs.getRange("A4:E4").format.font.bold = true;
expectedAs.getRange("A4:E4").format.fill.color = "#C6E0B4";
expectedAs.getRange("A1:E10").format.wrapText = true;
expectedAs.getRange("A1:E10").format.verticalAlignment = "Top";
expectedAs.getRange("A1:E10").format.font.name = "Arial";
expectedAs.getRange("A1:E10").format.font.size = 10;
expectedAs.getRange("A:A").format.columnWidth = 70;
expectedAs.getRange("B:B").format.columnWidth = 280;
expectedAs.getRange("C:E").format.columnWidth = 310;
expectedAs.getRange("A5:E10").format.rowHeight = 92;

// Keep the source layout but make the EV case easier to read.
sheet.getRange("A1:B1").format.font.bold = true;
sheet.getRange("A1:B1").format.fill.color = "#D9EAF7";
sheet.getRange("A1:B81").format.wrapText = true;
sheet.getRange("A1:B81").format.verticalAlignment = "Top";
sheet.getRange("A1:B81").format.font.name = "Arial";
sheet.getRange("A1:B81").format.font.size = 10;
sheet.getRange("A2:B81").format.rowHeight = 72;
sheet.getRange("A:A").format.columnWidth = 270;
sheet.getRange("B:B").format.columnWidth = 520;
sheet.getRange("C:D").format.columnWidth = 30;

await fs.mkdir(path.dirname(outputPath), { recursive: true });
const exported = await SpreadsheetFile.exportXlsx(workbook);
await exported.save(outputPath);

console.log(outputPath);
