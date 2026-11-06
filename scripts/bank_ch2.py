# scripts/bank_ch2.py
# 67 Rigorous, Medium-Difficulty Questions for Chapter 2: Decision Models & 6-Step Problem Solving

BANK_CH2 = [
    # --- 2.1 Model Definition & Forms ---
    {
        "topic": "Model Definition & Forms",
        "question": "In business analytics, how is a 'Model' formally defined?",
        "correct": "An abstraction or representation of a real system, idea, or object that captures its essential features",
        "distractors": [
            "A comprehensive database schema storing every transactional record generated across corporate history",
            "A legally binding commercial procurement contract negotiated between enterprise corporate attorneys",
            "An exhaustive operational manual describing clerical office protocols and employee filing procedures"
        ],
        "explanation": "A model is an abstraction or representation of a real system, idea, or object that captures the most important features while omitting irrelevant complexity."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "Which of the following is NOT one of the three primary forms in which an analytical model can be expressed?",
        "correct": "Physical hardware blueprints detailing microchip electronic circuit architecture",
        "distractors": [
            "Written or verbal descriptions articulated in natural spoken language",
            "Visual displays, flowcharts, influence diagrams, and graphical plots",
            "Mathematical formulas, algebraic equations, and spreadsheet models"
        ],
        "explanation": "The three forms of models are: (1) Written/verbal descriptions, (2) Visual displays/graphics, and (3) Mathematical/spreadsheet formulas."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "A marketing manager states: 'As advertising expenditure expands, sales volume grows rapidly at first, then eventually plateaus.' This expression is:",
        "correct": "A written or verbal model describing the functional relationship between promotion and sales",
        "distractors": [
            "A mathematical model containing formal algebraic equations and solved calculus derivatives",
            "A visual graphical display plotting advertising expenditure on a two-dimensional Cartesian plane",
            "A prescriptive optimization algorithm calculating exact corporate profit margins for finance"
        ],
        "explanation": "Describing a system relationship using spoken or written natural language is a verbal/written model."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "A sales analyst plots weekly marketing spend against unit sales on a scatter chart with a fitted trendline. This representation is:",
        "correct": "A visual graphical model illustrating the functional relationship between two variables",
        "distractors": [
            "A verbal model relying strictly on narrative paragraphs without quantitative figures",
            "A stochastic search heuristic designed to locate approximate local minima in code",
            "A deterministic linear programming model guaranteeing global profit maximization"
        ],
        "explanation": "Graphical charts, plots, and visual diagrams represent the visual/graphical form of a model."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "The adoption lifecycle of breakthrough consumer electronics (such as the first-generation iPad or 3D televisions) typically follows:",
        "correct": "An S-shaped growth curve, where sales initially accelerate through word-of-mouth before maturing",
        "distractors": [
            "A strictly linear downward slope, where customer demand contracts continuously from launch date",
            "A cyclical sine-wave curve, oscillating between zero and peak volume at regular monthly intervals",
            "A perfectly horizontal flat line, indicating that consumer demand remains static across years"
        ],
        "explanation": "New product adoption often follows an S-shaped curve: early growth accelerates as positive customer feedback spreads, then stabilizes as the market matures."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "In the mathematical S-curve formula S = a * e^(b * e^(c * t)), what does the variable 'S' represent?",
        "correct": "The unit sales volume achieved at time period t",
        "distractors": [
            "The mathematical base of natural logarithms",
            "The fixed manufacturing overhead cost per plant",
            "The promotional percentage discount offered in stores"
        ],
        "explanation": "In the adoption model S = a * e^(b * e^(c * t)), S represents sales volume, t represents time, e is the natural log base, and a, b, c are constants."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "Why do decision makers rely on models rather than experimenting directly on live business operations?",
        "correct": "Models allow risk-free experimentation and scenario testing without costly real-world disruptions",
        "distractors": [
            "Models are legally required by international financial auditing standards for every commercial purchase",
            "Real-world operational systems cannot be observed, recorded, or measured using corporate software",
            "Models guarantee that every future business policy will achieve complete operational success"
        ],
        "explanation": "Models provide a safe, cost-effective sandbox to evaluate decisions, analyze risks, and test hypotheses without disrupting live business systems."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "An influence diagram showing how Fixed Cost and Variable Cost combine to determine Total Cost is an example of:",
        "correct": "A visual model illustrating relationships among model components",
        "distractors": [
            "A prescriptive stochastic optimization model for warehouse location",
            "A narrative employee agreement defining performance salary metrics",
            "An automated heuristic search algorithm solving vehicle fleet routes"
        ],
        "explanation": "An influence diagram is a visual display that shows how various model elements and intermediate variables relate to one another."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "Which of the following describes the primary role of mathematical models in business analytics?",
        "correct": "Translating conceptual relationships into precise formulas to calculate outputs from inputs",
        "distractors": [
            "Replacing executive leadership and human management with automated transactional hardware",
            "Eliminating the requirement to collect and clean historical empirical business data feeds",
            "Protecting enterprise proprietary trade secrets from external competitor intelligence"
        ],
        "explanation": "Mathematical models formalize relationships into equations, enabling quantitative analysis, prediction, and optimization."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "When formulating an analytical model, what is the consequence of including too many minor real-world details?",
        "correct": "The model becomes overly complex, difficult to interpret, and prone to overfitting noise",
        "distractors": [
            "The model automatically transforms into a legally binding corporate financial charter",
            "The model's mathematical calculations will be rejected by enterprise relational database servers",
            "The model is guaranteed to identify the globally optimal business decision in every instance"
        ],
        "explanation": "A model must capture essential features; excessive complexity makes models cumbersome, uninterpretable, and fragile."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "What is the relationship between the three forms of models (verbal, visual, and mathematical)?",
        "correct": "They are complementary perspectives that can represent the exact same underlying business system",
        "distractors": [
            "They are mutually exclusive representations that cannot be combined within a single enterprise",
            "Verbal models are restricted to human resources, while visual models are exclusive to marketing",
            "Mathematical models must always be completely finalized before verbal models can be conceived"
        ],
        "explanation": "A single business system can be expressed verbally, visually (diagrams/charts), and mathematically (equations) to communicate with different stakeholders."
    },
    {
        "topic": "Model Definition & Forms",
        "question": "In the S-curve adoption model S = a * e^(b * e^(c * t)), what role do the letters 'a', 'b', and 'c' play?",
        "correct": "They are mathematical constants that define the scale, inflection point, and growth rate of the curve",
        "distractors": [
            "They represent controllable marketing decisions such as price, advertising, and coupon value",
            "They denote uncontrollable external variables like annual inflation and unemployment rates",
            "They represent the output performance measures including net profit, gross margin, and tax rate"
        ],
        "explanation": "In S = a * e^(b * e^(c * t)), a, b, and c are structural model constants/parameters estimated from market data."
    },

    # --- 2.2 Decision Model Architecture: Inputs to Outputs ---
    {
        "topic": "Decision Model Architecture",
        "question": "What is the primary function of a 'Decision Model' in business analytics?",
        "correct": "To understand, analyze, or facilitate managerial decision making by evaluating inputs and outputs",
        "distractors": [
            "To record routine accounting transactions into the company's enterprise general ledger",
            "To enforce network security policies across employee workstations and mobile phones",
            "To design architectural floor plans and structural engineering blueprints for factories"
        ],
        "explanation": "A decision model is defined as a model specifically developed to understand, analyze, or facilitate decision making."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "Which of the following lists correctly identifies the three primary categories of inputs in a decision model?",
        "correct": "Data, Uncontrollable Variables, and Decision Variables (Controllable)",
        "distractors": [
            "Internal Audits, External Lawsuits, and Corporate Tax Withholdings",
            "Desktop Hardware, Cloud Infrastructure, and Ethernet Network Switches",
            "Customer Complaints, Cash Receipts, and Annual Performance Reviews"
        ],
        "explanation": "Decision models process three input types: Data (known constants), Uncontrollable Variables (external environment), and Decision Variables (controllable choices)."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "In a retail pricing decision model, how is the 'selling price per unit' classified?",
        "correct": "A Decision Variable, because management has direct authority to choose and manipulate its value",
        "distractors": [
            "An Uncontrollable Variable, because commodity market conditions govern all consumer behavior",
            "Constant Data, because corporate prices are fixed permanently by enterprise accounting rules",
            "A Behavioral Output, because price represents a psychological feeling experienced by consumers"
        ],
        "explanation": "Decision variables are inputs that decision makers have direct control over, such as retail price, advertising spend, or production volume."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "In an airline profitability model, how should the 'future market price of jet fuel' be classified?",
        "correct": "An Uncontrollable Variable, because global energy prices are determined by external market forces",
        "distractors": [
            "A Decision Variable, because airline managers can vote to set the price of commercial fuel",
            "Constant Data, because petroleum prices remain identical every single month across decades",
            "A Performance Output, because fuel price represents the net financial profit of the airline"
        ],
        "explanation": "Uncontrollable variables are external factors dictated by markets, nature, or competitors that management cannot directly control."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "In a production planning model, which of the following is the best example of 'Data' (as an input)?",
        "correct": "The known physical machine capacity of 40 operational hours per week per assembly line",
        "distractors": [
            "The quantity of units management chooses to schedule for production on Monday morning",
            "The future inflation rate of industrial metal commodities over the next five years",
            "The net operating margin realized by the manufacturing company at fiscal year end"
        ],
        "explanation": "Data inputs are known, established constants or parameters (such as physical machine capacity or standard labor hours per unit)."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "What are the two major categories of outputs generated by a decision model?",
        "correct": "Performance measures and Behavioral measures",
        "distractors": [
            "Hardware metrics and Network protocols",
            "Employee payroll and Vendor contracts",
            "Unprocessed spreadsheets and Raw error logs"
        ],
        "explanation": "Decision model outputs consist of Performance measures (e.g. profit, cost, ROI) and Behavioral measures (e.g. customer response, queue lengths)."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "In a bank branch simulation model, which output is classified as a 'Behavioral Measure'?",
        "correct": "The average waiting time customers tolerate in line before abandoning the branch",
        "distractors": [
            "The total quarterly net interest income earned across all commercial checking accounts",
            "The statutory corporate income tax rate mandated by national government revenue services",
            "The hourly wage paid to certified bank tellers under union employment agreements"
        ],
        "explanation": "Customer queuing patience and abandonment behaviors are Behavioral measures, reflecting how human agents react within the system."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "In a corporate decision model, which output is classified as a 'Performance Measure'?",
        "correct": "Net profit, return on capital invested, and total manufacturing overhead cost",
        "distractors": [
            "The consumer sentiment rating of competing fashion brands on digital social media",
            "The probability that a customer visits the store on a rainy afternoon rather than sunny",
            "The statutory corporate minimum wage set by municipal regulatory authorities"
        ],
        "explanation": "Performance measures evaluate organizational success, financial outcomes, efficiency, and economic returns."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "Consider the grocery sales-promotion model: Sales = 500 - 0.05(Price) + 30(Coupons) + 0.08(Adv) + 0.25(Price)(Adv). What does the term '0.25(Price)(Adv)' represent?",
        "correct": "An interaction effect showing that the effectiveness of advertising increases at higher price points",
        "distractors": [
            "The fixed overhead rent expense incurred by the grocery store chain regardless of sales",
            "A mathematical penalty for charging customers checkout convenience fees during holidays",
            "A deterministic constraint stating that advertising expenditure cannot exceed retail price"
        ],
        "explanation": "An interaction term captures synergy: here, advertising effectiveness has a stronger impact on sales when the product is priced higher."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "Using the model Sales = 500 - 0.05(Price) + 30(Coupons) + 0.08(Adv) + 0.25(Price)(Adv), what are the controllable decision variables?",
        "correct": "Price, Coupons (0 or 1), and Advertising expenditure",
        "distractors": [
            "Sales volume, Total Revenue, and Grocery store market share",
            "Customer foot traffic, Regional weather, and Competitor advertising",
            "The intercept coefficient 500 and the interaction weight 0.25"
        ],
        "explanation": "Store managers choose price, whether to distribute coupons, and how much to spend on advertising; these are controllable decision variables."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "Suppose a grocery store sets Price = $10, Coupons = 1 (yes), and Advertising = $100. Using Sales = 500 - 0.05(10) + 30(1) + 0.08(100) + 0.25(10)(100), what is predicted Sales?",
        "correct": "787.5 units",
        "distractors": [
            "537.5 units",
            "1,250.0 units",
            "620.0 units"
        ],
        "explanation": "Sales = 500 - 0.5 + 30 + 8 + 250 = 787.5 units."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "In the grocery sales-promotion model, why is 'Coupons' treated as an indicator (0, 1) variable?",
        "correct": "It represents a binary managerial decision: either a coupon campaign is run (1) or not run (0)",
        "distractors": [
            "Because retail cash register scanners are incapable of reading values larger than one",
            "Because coupons lose their promotional value within twenty-four hours of distribution",
            "Because commercial grocers are legally restricted from distributing multiple coupon flyers"
        ],
        "explanation": "An indicator (dummy) variable taking values 0 or 1 models binary choices, such as offering coupons or not."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "What happens in a decision model when an analyst incorrectly treats an uncontrollable variable as a controllable decision variable?",
        "correct": "Management produces unrealistic operational plans that assume control over external market forces",
        "distractors": [
            "The relational database schema corrupts all foreign key indexing tables automatically",
            "Enterprise suppliers become legally bound to reduce their wholesale raw material prices",
            "The mathematical optimization solver permanently locks out analytical user permissions"
        ],
        "explanation": "Treating uncontrollable external forces (like competitor pricing or inflation) as internal choices produces fantasy-based, unexecutable plans."
    },
    {
        "topic": "Decision Model Architecture",
        "question": "Which of the following represents an Uncontrollable Variable for an agricultural farming enterprise?",
        "correct": "Seasonal rainfall volume and global commodity market crop prices",
        "distractors": [
            "The volume of chemical fertilizer applied per acre of cultivated cropland",
            "The specific brand and model of harvesting tractors acquired by the farm",
            "The hourly wage rate offered to seasonal fruit-picking agricultural laborers"
        ],
        "explanation": "Weather and global commodity prices are uncontrollable external variables, whereas fertilizer amounts and equipment purchases are controllable choices."
    },

    # --- 2.3 Descriptive Decision Models & Break-Even Analysis ---
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "What is the defining characteristic of a 'Descriptive Decision Model'?",
        "correct": "It describes relationships and states 'what is', but does not tell managers what decision to make",
        "distractors": [
            "It automatically executes corporate payroll disbursements through commercial banking clearing houses",
            "It identifies the single mathematically optimal decision that guarantees maximum commercial profit",
            "It forecasts macroeconomic events ten years into the future with absolute mathematical certainty"
        ],
        "explanation": "Descriptive decision models describe existing relationships and system behaviors ('what is'); they do not prescribe optimal actions."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "In the standard Total Cost equation TC = F + V * Q, what does 'V' represent?",
        "correct": "The variable cost incurred to produce a single unit of output",
        "distractors": [
            "The fixed overhead rent expense incurred regardless of production volume",
            "The total quantity of finished goods manufactured and shipped to retailers",
            "The retail selling price charged to final consumers in department stores"
        ],
        "explanation": "In TC = F + V * Q, F is fixed cost, V is unit variable cost, and Q is production volume."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "In a manufacturing break-even decision model, what is the 'Break-Even Point'?",
        "correct": "The production volume where total revenue equals total cost, resulting in zero profit and zero loss",
        "distractors": [
            "The maximum theoretical physical output capacity of an industrial manufacturing plant",
            "The exact corporate calendar date when all commercial bank debt obligations are retired",
            "The price threshold where consumer demand drops to zero units due to consumer resistance"
        ],
        "explanation": "The break-even point is the volume where Total Revenue equals Total Cost (or where two alternative production options incur identical total cost)."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "A manufacturer is deciding between making a component in-house or outsourcing. In-house cost is TC(m) = $50,000 + $125*Q. Outsourcing cost is TC(o) = $175*Q. What is the break-even volume?",
        "correct": "1,000 units",
        "distractors": [
            "500 units",
            "2,500 units",
            "400 units"
        ],
        "explanation": "Set TC(m) = TC(o): $50,000 + $125*Q = $175*Q -> $50*Q = $50,000 -> Q = 1,000 units."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "In the make-or-buy model TC(m) = $50,000 + $125*Q and TC(o) = $175*Q, if projected demand is 600 units, which option is more economical?",
        "correct": "Outsourcing, because TC(o) = $105,000 while TC(m) = $125,000",
        "distractors": [
            "Manufacturing, because TC(m) = $75,000 while TC(o) = $105,000",
            "Both options incur identical costs because 600 units exceeds fixed costs",
            "Neither option is viable because production volume must exceed 2,000 units"
        ],
        "explanation": "For Q = 600: TC(m) = 50000 + 125(600) = $125,000. TC(o) = 175(600) = $105,000. Outsourcing saves $20,000."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "In the make-or-buy model TC(m) = $50,000 + $125*Q and TC(o) = $175*Q, what is the general managerial decision rule?",
        "correct": "Outsource for production volumes below 1,000 units; manufacture in-house for volumes above 1,000 units",
        "distractors": [
            "Manufacture in-house for volumes below 1,000 units; outsource for volumes above 1,000 units",
            "Outsource under all circumstances because fixed costs should never be incurred by any business",
            "Manufacture in-house under all circumstances because variable costs are irrelevant to profit"
        ],
        "explanation": "Below break-even (Q < 1000), avoiding fixed costs makes outsourcing cheaper; above 1000 units, lower variable cost ($125 vs $175) makes in-house production economical."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "In standard cost-volume-profit analysis, what is the 'Contribution Margin per Unit'?",
        "correct": "The selling price per unit minus the variable cost per unit (P - V)",
        "distractors": [
            "The total fixed cost divided by the statutory annual corporate tax rate",
            "The sum of total revenue and total factory depreciation expense",
            "The retail price multiplied by the number of units returned by customers"
        ],
        "explanation": "Unit contribution margin is (P - V), representing the portion of each unit's selling price that contributes toward covering fixed overhead costs."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "If a company has Fixed Costs F = $120,000, Unit Variable Cost V = $30, and Selling Price P = $70, what is the break-even volume in units?",
        "correct": "3,000 units",
        "distractors": [
            "1,714 units",
            "4,000 units",
            "1,200 units"
        ],
        "explanation": "Unit contribution margin = $70 - $30 = $40. Q_BE = F / (P - V) = $120,000 / $40 = 3,000 units."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "What happens to the break-even quantity (Q_BE) if unit variable costs increase while fixed costs and selling price remain unchanged?",
        "correct": "The break-even quantity increases, requiring higher sales volume to cover fixed overhead",
        "distractors": [
            "The break-even quantity decreases, allowing the firm to reach profitability much faster",
            "The break-even quantity remains completely unchanged because fixed costs did not move",
            "The break-even quantity instantly drops to zero units due to reduced contribution"
        ],
        "explanation": "Higher unit variable cost reduces unit contribution margin (P - V), meaning more units must be sold to cover fixed costs F."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "Why does an Influence Diagram serve as an effective communication tool in descriptive modeling?",
        "correct": "It visually maps dependencies and relationships among inputs, intermediate variables, and outputs",
        "distractors": [
            "It compiles Python source code into machine-executable binary libraries for cloud clusters",
            "It proves mathematically that the chosen decision model contains zero statistical errors",
            "It legally certifies corporate financial statements for filing with national tax agencies"
        ],
        "explanation": "Influence diagrams provide intuitive visual clarity on how inputs, intermediate factors, and final performance measures connect."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "In an influence diagram for Total Cost, which two elements directly link into Total Cost?",
        "correct": "Fixed Cost and Variable Cost",
        "distractors": [
            "Corporate Tax Rate and Employee Healthcare Benefit Deductions",
            "Executive Stock Options and Office Facility Maintenance Charges",
            "Retail Shelf Space and Competitor Television Advertising Hours"
        ],
        "explanation": "In an influence diagram for Total Cost, Fixed Cost and Variable Cost feed directly into Total Cost (where Variable Cost is influenced by Unit Variable Cost and Quantity)."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "If a firm expects demand to be 1,500 units in the make-or-buy model TC(m) = $50,000 + $125*Q vs TC(o) = $175*Q, how much money is saved by manufacturing in-house?",
        "correct": "$25,000",
        "distractors": [
            "$50,000",
            "$12,500",
            "$35,000"
        ],
        "explanation": "TC(m) = 50,000 + 125(1500) = $237,500. TC(o) = 175(1500) = $262,500. Savings = $262,500 - $237,500 = $25,000."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "What is the Total Cost incurred at the exact break-even point of 1,000 units in the make-or-buy model TC(m) = $50,000 + $125*Q vs TC(o) = $175*Q?",
        "correct": "$175,000",
        "distractors": [
            "$125,000",
            "$200,000",
            "$50,000"
        ],
        "explanation": "At Q = 1000, TC(o) = 175 * 1000 = $175,000; TC(m) = 50,000 + 125 * 1000 = $175,000."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "Which of the following is an underlying assumption of simple linear break-even decision models?",
        "correct": "Unit variable cost and selling price remain constant regardless of the production volume",
        "distractors": [
            "Fixed costs double automatically every time production increases by a single unit",
            "Consumer demand is completely independent of the price charged by the company",
            "Outsourcing vendors must always charge lower prices than in-house factories"
        ],
        "explanation": "Basic linear break-even models assume constant unit variable costs and constant selling price over the relevant volume range."
    },
    {
        "topic": "Descriptive Models & Break-Even",
        "question": "If a factory's fixed overhead rent doubles from $50,000 to $100,000, while variable costs remain $125 and outsourcing remains $175, what is the new break-even point?",
        "correct": "2,000 units",
        "distractors": [
            "1,500 units",
            "1,000 units",
            "3,000 units"
        ],
        "explanation": "Q_BE = F / (175 - 125) = $100,000 / $50 = 2,000 units."
    },

    # --- 2.4 Demand Prediction Models: Linear vs. Non-Linear ---
    {
        "topic": "Demand Prediction Models",
        "question": "In a linear demand prediction model D = a - b * P, what does the parameter 'b' represent?",
        "correct": "The constant rate at which unit demand falls for each one-dollar increase in price",
        "distractors": [
            "The maximum theoretical unit demand when price is set to infinity",
            "The percentage change in consumer household disposable income",
            "The fixed manufacturing overhead cost required to produce one unit"
        ],
        "explanation": "In D = a - b * P, -b is the slope, representing the constant absolute reduction in demand for each unit increase in price."
    },
    {
        "topic": "Demand Prediction Models",
        "question": "Using the linear demand model D = 20,000 - 10 * P, what is the predicted demand if price is set to $100?",
        "correct": "19,000 units",
        "distractors": [
            "19,200 units",
            "18,000 units",
            "10,000 units"
        ],
        "explanation": "D = 20,000 - 10(100) = 20,000 - 1,000 = 19,000 units."
    },
    {
        "topic": "Demand Prediction Models",
        "question": "Using the linear demand model D = 20,000 - 10 * P, if price is raised from $80 to $110, by how much does demand change?",
        "correct": "Demand decreases by 300 units",
        "distractors": [
            "Demand increases by 300 units",
            "Demand decreases by 1,100 units",
            "Demand remains completely unchanged"
        ],
        "explanation": "Change in price = $30. Change in demand = -10 * 30 = -300 units (falls from 19,200 to 18,900)."
    },
    {
        "topic": "Demand Prediction Models",
        "question": "What is a primary characteristic of a Non-linear Demand Model formulated as D = a * P^(-b)?",
        "correct": "It assumes a constant price elasticity of demand across all price levels",
        "distractors": [
            "It assumes demand drops by the exact same number of units for every dollar price hike",
            "It predicts that demand will reach zero as soon as price rises above one dollar",
            "It represents a purely descriptive model that cannot be computed on spreadsheets"
        ],
        "explanation": "The power formulation D = a * P^(-b) assumes constant price elasticity (the ratio of % change in demand to % change in price is constant)."
    },
    {
        "topic": "Demand Prediction Models",
        "question": "How does price elasticity behave in a Linear Demand Model D = a - b * P compared to a Power Model D = a * P^(-b)?",
        "correct": "Elasticity varies at every point along a linear curve, but remains constant in the power model",
        "distractors": [
            "Elasticity is constant along a linear curve, but varies wildly in the power model",
            "Both models exhibit perfectly constant elasticity across all positive price points",
            "Neither model can be used to calculate price elasticity under any circumstances"
        ],
        "explanation": "A linear demand curve has varying elasticity at different price points, whereas D = a * P^(-b) exhibits constant price elasticity of -b everywhere."
    },
    {
        "topic": "Demand Prediction Models",
        "question": "In the non-linear demand model D = 20,000 * P^(-0.03), what does the exponent -0.03 represent?",
        "correct": "The price elasticity of demand, indicating a 0.03% demand decrease for each 1% price increase",
        "distractors": [
            "The maximum unit sales volume achievable when product price is set to zero",
            "The annual interest rate charged on overdue retail consumer credit card accounts",
            "The fixed manufacturing cost required to retool automated factory assembly lines"
        ],
        "explanation": "The exponent in D = a * P^(-b) represents price elasticity: here, a 1% price increase leads to a 0.03% drop in demand."
    },
    {
        "topic": "Demand Prediction Models",
        "question": "Why do economists often prefer non-linear demand models over linear models for broad pricing ranges?",
        "correct": "Linear models predict unrealistic negative demand at high prices and infinite demand at zero price",
        "distractors": [
            "Linear models cannot be graphed on two-dimensional Cartesian coordinate charts",
            "Non-linear models are legally mandated for publicly traded commercial enterprise filings",
            "Non-linear models guarantee that corporate net revenue will never decline"
        ],
        "explanation": "Linear models hit negative values at high prices; non-linear curves better reflect asymptotic consumer behavior over wide price ranges."
    },
    {
        "topic": "Demand Prediction Models",
        "question": "In demand modeling, what is the formal definition of 'Price Elasticity of Demand'?",
        "correct": "The ratio of the percentage change in demand to the percentage change in price",
        "distractors": [
            "The total monetary value of unsold inventory left on store shelves at month end",
            "The absolute dollar increase in factory overhead costs caused by wage increases",
            "The speed at which manufacturing supply chains can ship replacement components"
        ],
        "explanation": "Price elasticity of demand is defined as (% change in quantity demanded) / (% change in price)."
    },
    {
        "topic": "Demand Prediction Models",
        "question": "If price elasticity of demand is -0.03, consumer demand for this product is considered:",
        "correct": "Highly inelastic, meaning consumers are very insensitive to price changes",
        "distractors": [
            "Highly elastic, meaning a tiny price increase causes demand to crash to zero",
            "Unitary elastic, meaning total corporate revenue remains perfectly identical",
            "Completely random, meaning prices and sales volume have zero statistical correlation"
        ],
        "explanation": "An elasticity with absolute value well below 1 (0.03) is highly inelastic; quantity demanded barely changes when price moves."
    },

    # --- 2.5 Prescriptive Decision Models & Optimization ---
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "What is the primary objective of a 'Prescriptive Decision Model'?",
        "correct": "To help decision makers identify and select the best (optimal) course of action",
        "distractors": [
            "To provide a historical summary table of past quarterly inventory movements",
            "To visually display organizational hierarchies and executive reporting chains",
            "To measure employee keystroke counts during customer support telephone calls"
        ],
        "explanation": "Prescriptive decision models aim to find the best course of action by optimizing an objective function subject to constraints."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "In mathematical optimization, what is the 'Objective Function'?",
        "correct": "The mathematical equation that decision makers seek to maximize (e.g. profit) or minimize (e.g. cost)",
        "distractors": [
            "The list of corporate legal policies published in the annual employee code of conduct",
            "The physical floor plan diagram showing warehouse forklift transit aisles and storage bays",
            "The chronological project timeline tracking software sprint completion dates"
        ],
        "explanation": "The objective function is the core mathematical formula that quantifies the goal to be optimized (e.g. maximizing profit or minimizing cost)."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "In an optimization model, what are 'Constraints'?",
        "correct": "Physical, financial, or operational limitations and restrictions imposed on decision variables",
        "distractors": [
            "The calculated performance measures that appear in the final executive dashboard",
            "The historical transaction records archived in offsite magnetic tape vaults",
            "The natural log base constants used in non-linear exponential adoption curves"
        ],
        "explanation": "Constraints are restrictions or limitations (e.g. budget limits, labor capacity, machine hours) restricting decision variable choices."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "What is an 'Optimal Solution' in an optimization decision model?",
        "correct": "The decision variable values that optimize the objective function while satisfying all constraints",
        "distractors": [
            "The initial heuristic guess entered by an analyst before executing any mathematical calculations",
            "The production volume where outsourcing cost equals manufacturing cost exactly",
            "Any feasible decision variable values that satisfy at least one operational machine constraint"
        ],
        "explanation": "An optimal solution is the feasible set of decision variables that produces the best possible objective function value without violating any constraints."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "Analysts determine the demand model Sales = -2.9485 * Price + 3240.9. Total Revenue is (Price) * (Sales). What is the total revenue equation?",
        "correct": "Total Revenue = -2.9485 * (Price)^2 + 3240.9 * Price",
        "distractors": [
            "Total Revenue = -2.9485 * Price + 3240.9",
            "Total Revenue = 3240.9 / Price - 2.9485",
            "Total Revenue = (Price)^2 - 2.9485 * Price + 3240.9"
        ],
        "explanation": "Total Revenue = Price * Sales = Price * (-2.9485 * Price + 3240.9) = -2.9485 * Price^2 + 3240.9 * Price."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "In the pricing model Total Revenue = -2.9485 * P^2 + 3240.9 * P, how is the price that maximizes revenue found?",
        "correct": "By taking the first derivative with respect to Price, setting it to zero, and solving for P",
        "distractors": [
            "By setting Price equal to zero and calculating the resulting customer demand",
            "By multiplying the fixed costs by the statutory corporate tax withholding rate",
            "By outsourcing production to an external vendor whenever price exceeds $100"
        ],
        "explanation": "To maximize a quadratic concave function TR = a*P^2 + b*P, set d(TR)/dP = 2a*P + b = 0, so P = -b / (2a)."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "Using TR = -2.9485 * P^2 + 3240.9 * P, what is the approximate revenue-maximizing price P*?",
        "correct": "$549.57",
        "distractors": [
            "$324.09",
            "$1,100.00",
            "$175.00"
        ],
        "explanation": "d(TR)/dP = -5.897 * P + 3240.9 = 0 -> P = 3240.9 / 5.897 ≈ $549.57."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "What is the key difference between a Deterministic Model and a Stochastic Model?",
        "correct": "Deterministic models assume all inputs are known with certainty; stochastic models incorporate probabilistic uncertainty",
        "distractors": [
            "Deterministic models are executed on desktop workstations; stochastic models run on distributed clusters",
            "Deterministic models focus strictly on cost minimization; stochastic models evaluate revenue expansion",
            "Deterministic models are utilized by commercial banks; stochastic models are restricted to universities"
        ],
        "explanation": "Deterministic models have known, certain parameters; stochastic models involve random variables or probability distributions."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "In predictive and prescriptive modeling, how are 'Uncertainty' and 'Risk' formally distinguished?",
        "correct": "Uncertainty is imperfect knowledge of future outcomes; risk is associated with the consequences of what actually occurs",
        "distractors": [
            "Uncertainty refers strictly to financial debt ratios; risk refers to physical machinery breakdown frequency",
            "Uncertainty can be completely eliminated by insurance; risk cannot be analyzed using mathematics",
            "Uncertainty applies only to marketing initiatives; risk applies only to corporate accounting statements"
        ],
        "explanation": "Uncertainty is imperfect knowledge of what will happen in the future; risk is associated with the consequences/costs of what actually occurs."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "A supply chain model incorporates supplier delivery delays modeled as normal probability distributions. This model is:",
        "correct": "A Stochastic Model, because key input parameters are governed by probability distributions",
        "distractors": [
            "A Deterministic Model, because delivery delays can be eliminated through contract clauses",
            "A Descriptive Influence Diagram, because it cannot be solved using numerical algorithms",
            "A Pure Linear Break-Even Model, because fixed costs equal zero across all warehouses"
        ],
        "explanation": "Because key inputs are characterized by probability distributions rather than known certainties, it is a Stochastic model."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "In decision analytics, how is an 'Algorithm' formally defined?",
        "correct": "A systematic, step-by-step mathematical procedure used to find an optimal solution to a decision model",
        "distractors": [
            "A visual slide presentation delivered to corporate board members at fiscal year-end",
            "An unorganized collection of customer feedback comments downloaded from web forums",
            "A proprietary computer operating system licensed exclusively to retail banking branches"
        ],
        "explanation": "An algorithm is a systematic, sequential procedure designed to solve a mathematical model and find an optimal solution."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "When are 'Search Algorithms' (heuristics) used in place of exact optimization algorithms?",
        "correct": "For highly complex problems where finding a guaranteed optimal solution is computationally intractable",
        "distractors": [
            "When the business organization has zero access to electronic computers or spreadsheets",
            "When government regulations prohibit corporations from maximizing their commercial profits",
            "When all model input parameters and constraints are known with 100% absolute certainty"
        ],
        "explanation": "Search algorithms (heuristics) are used for complex or large-scale problems to find good/near-optimal solutions when exact algorithms take too long."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "What is a known limitation of using Search Algorithms (heuristics) in business decision modeling?",
        "correct": "They find good, practical solutions but do not guarantee that the solution found is globally optimal",
        "distractors": [
            "They can only process datasets that contain fewer than ten total records",
            "They automatically delete historical database tables upon completion of execution",
            "They are legally invalid for use in commercial private enterprise logistics"
        ],
        "explanation": "Search algorithms trade global optimality guarantees for computational speed and tractability on complex problems."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "Which of the following is an example of a Deterministic Prescriptive Model?",
        "correct": "A linear programming model assigning factory production schedules with known costs and capacities",
        "distractors": [
            "A Monte Carlo simulation evaluating portfolio returns under random currency fluctuations",
            "A queuing simulation assessing patient emergency room wait times with random arrival rates",
            "A Markov chain predicting consumer brand switching probabilities under volatile marketing"
        ],
        "explanation": "Linear programming with known, constant parameters and capacities is a classic deterministic prescriptive model."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "Why do predictive decision models often incorporate uncertainty?",
        "correct": "To help decision makers analyze potential risks and assess the probability of adverse outcomes",
        "distractors": [
            "To deliberately obscure commercial performance metrics from external regulatory inspection",
            "To comply with corporate financial reporting guidelines requiring synthetic variance noise",
            "Because modern computer processors are incapable of executing deterministic math equations"
        ],
        "explanation": "Incorporating uncertainty allows managers to assess risk, evaluate probability distributions of outcomes, and prepare contingency plans."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "Which of the following business problems is best addressed using Prescriptive Optimization rather than Predictive Modeling?",
        "correct": "Determining the optimal dispatch routing for 50 delivery trucks to minimize total fuel consumption",
        "distractors": [
            "Estimating the likelihood that an online shopper will purchase a product during Black Friday",
            "Forecasting quarterly regional electricity consumption based on historical summer weather",
            "Classifying incoming customer service emails into billing, technical, and sales categories"
        ],
        "explanation": "Route optimization involves selecting decision variables (routes) to minimize an objective (fuel) subject to constraints (delivery windows)."
    },
    {
        "topic": "Prescriptive Models & Optimization",
        "question": "What is the relationship between Business Analytics and the broader process of problem solving and decision making?",
        "correct": "Business Analytics represents an important analytical portion, but not the entirety of the process",
        "distractors": [
            "Business Analytics completely replaces all human managerial judgment, ethics, and leadership",
            "Business Analytics is only relevant during the final implementation step of problem solving",
            "Problem solving and decision making are entirely qualitative and can never utilize analytics"
        ],
        "explanation": "Analytics provides powerful quantitative tools, but is only one component of the broader problem-solving process that includes human judgment."
    },

    # --- 2.6 The 6-Step Problem Solving Framework & HP Guidelines ---
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "What is the correct sequential order of the 6 steps in the problem solving and decision making process?",
        "correct": "Recognizing -> Defining -> Structuring -> Analyzing -> Interpreting & Deciding -> Implementing",
        "distractors": [
            "Defining -> Recognizing -> Analyzing -> Structuring -> Implementing -> Interpreting",
            "Structuring -> Recognizing -> Defining -> Analyzing -> Interpreting -> Implementing",
            "Analyzing -> Defining -> Structuring -> Recognizing -> Implementing -> Deciding"
        ],
        "explanation": "The six steps are: (1) Recognizing, (2) Defining, (3) Structuring, (4) Analyzing, (5) Interpreting results & making a decision, (6) Implementing the solution."
    },
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "According to the 6-step framework, when does a problem formally exist?",
        "correct": "When there is a noticeable gap between what is currently happening and what should be happening",
        "distractors": [
            "When corporate computer servers reach maximum storage capacity in data centers",
            "When enterprise management hires external strategy consulting partners for review",
            "When regulatory authorities request routine annual tax documentation filings"
        ],
        "explanation": "A problem exists when there is a perceived gap between current actual performance and desired/expected performance."
    },
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "Why is Step 2 ('Defining the Problem') considered the most challenging step in the problem solving process?",
        "correct": "Real-world problems involve competing objectives, multiple stakeholders, and hidden root causes",
        "distractors": [
            "Relational database management systems corrupt tabular indexes when text definitions exceed limits",
            "Enterprise executives are legally prohibited from communicating directly with analytical specialists",
            "Mathematical formulas cannot be drafted until all corporate business units achieve consensus"
        ],
        "explanation": "Defining problems is difficult because symptoms mask causes, objectives conflict, multiple stakeholders are affected, and constraints exist."
    },
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "Which of the following factors does NOT increase the complexity of defining a business problem?",
        "correct": "Having a single, unified decision maker who possesses complete control and infinite time",
        "distractors": [
            "The presence of a large number of alternative courses of action available to the firm",
            "The existence of several competing and conflicting organizational business objectives",
            "A situation where the designated problem owner and the problem solver are different people"
        ],
        "explanation": "Having a single decision maker with clear control and no time pressure simplifies problem definition; competing objectives and multiple actors increase complexity."
    },
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "What primary activities take place during Step 3 ('Structuring the Problem')?",
        "correct": "Stating goals and objectives, characterizing possible decisions, and identifying operational constraints",
        "distractors": [
            "Installing database software drivers on local analytical workstation computers",
            "Negotiating annual salary bonuses with union labor representatives and managers",
            "Writing the final executive summary slide presentation for the board of directors"
        ],
        "explanation": "Structuring the problem involves stating goals, characterizing the decisions to be made, and identifying limitations and constraints."
    },
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "What primary activities occur during Step 4 ('Analyzing the Problem')?",
        "correct": "Applying appropriate business analytics techniques such as experimentation, statistical analysis, or optimization",
        "distractors": [
            "Conducting employee exit interviews to assess workplace cultural dissatisfaction",
            "Formulating the broad corporate mission statement published on the company website",
            "Drafting legal nondisclosure agreements for third-party commercial outsourcing vendors"
        ],
        "explanation": "Analyzing the problem involves identifying and applying appropriate BA techniques, statistical analysis, simulation, or optimization solvers."
    },
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "During Step 5 ('Interpreting Results and Making a Decision'), why must managers incorporate subjective judgment?",
        "correct": "Mathematical models simplify reality and cannot capture intangible factors, employee morale, or ethics",
        "distractors": [
            "Commercial optimization algorithms introduce random arithmetic noise into decision reports",
            "Quantitative models are legally barred from informing strategic commercial business policies",
            "Subjective intuition is mandated by regulatory accounting standards to calculate taxable revenue"
        ],
        "explanation": "Models are abstractions with limitations and assumptions; managerial judgment synthesizes quantitative outputs with qualitative context."
    },
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "What is essential for ensuring successful execution during Step 6 ('Implementing the Solution')?",
        "correct": "Translating mathematical model results into real-world workflows and providing training and resources",
        "distractors": [
            "Restricting model documentation to technical data scientists to preserve project exclusivity",
            "Automating operational staffing decisions completely without any human supervisory oversight",
            "Reverting to legacy manual record-keeping systems to verify computational algorithmic results"
        ],
        "explanation": "Implementation requires translating model findings into real-world processes, training staff, and securing adequate resources."
    },
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "According to the Hewlett-Packard (HP) analytics guidelines, what question should analysts answer BEFORE building a new model?",
        "correct": "'Will analytics actually solve the problem, and can we leverage an existing solution?'",
        "distractors": [
            "'Can we acquire the most costly enterprise cloud database infrastructure available?'",
            "'How many doctoral data science researchers can the human resources team recruit?'",
            "'Will this mathematical algorithm allow the company to eliminate frontline operations?'"
        ],
        "explanation": "HP guidelines advise asking: Will analytics solve the problem? Can we leverage an existing solution? Is a decision model really needed?"
    },
    {
        "topic": "6-Step Problem Solving Framework",
        "question": "The Hewlett-Packard (HP) analytics implementation guidelines recommend 'building insight, not black boxes.' What does this mean?",
        "correct": "Analytical tools should provide transparent, understandable logic that business users trust and comprehend",
        "distractors": [
            "Server hardware cases must be manufactured using transparent plastic casings in data centers",
            "Analysts must write application code without using modern high-level object-oriented programming",
            "Models should conceal all mathematical logic behind proprietary encrypted administrative passwords"
        ],
        "explanation": "Building insight rather than black boxes ensures stakeholders understand the drivers behind recommendations, fostering adoption and trust."
    }
]
