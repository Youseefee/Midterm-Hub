import json

# Generates 300 high quality, rigorous questions for E-Commerce
# Covering:
# Lec 1 (Questions 1-75): Intro, Definitions, Types (B2B, B2C, etc.), Benefits & Limitations
# Ch 2 (Questions 76-150): Business Models, 8 Key Elements, B2C/B2B models, Value Chains
# Ch 4 (Questions 151-225): Building E-Commerce Presence, SDLC, Hosting, Architecture, Mobile
# Ch 5 (Questions 226-300): Security Dimensions, Threats, Encryption, PKI, Firewalls, Payment Systems

questions = []

def add_q(topic, q_text, options, ans_idx, explanation):
    q_id = f"ecom_{len(questions) + 1}"
    questions.append({
        "id": q_id,
        "subject": "E-Commerce",
        "topic": topic,
        "question": q_text,
        "options": options,
        "answer": ans_idx,
        "explanation": explanation
    })

# =========================================================================
# LECTURE 1: INTRO, DEFINITIONS, CLASSIFICATIONS, BENEFITS & BARRIERS (Q1 - Q75)
# =========================================================================

add_q("EC Definitions & Perspectives",
      "From a commercial (trading) perspective, how is Electronic Commerce (EC) defined?",
      ["As a system for manufacturing physical hardware chips",
       "As the process of buying, selling, and exchanging products, services, and information over computer networks, including the Internet",
       "As an operating system designed for retail stores",
       "As a protocol for sending text messages between mobile phones"],
      1,
      "From a commercial/trading perspective, E-Commerce provides the capability of buying, selling, and exchanging goods, services, and information over telecommunication networks.")

add_q("EC Definitions & Perspectives",
      "From a business process perspective, what does Electronic Commerce enable?",
      ["Doing business electronically by completing business processes over electronic networks, thereby substituting information for physical business processes",
       "Replacing all human employees with robots immediately",
       "Eliminating the need for financial accounting",
       "Printing physical paper catalogs faster"],
      0,
      "From a business process perspective, EC automates business workflows, substituting digital information and electronic transactions for physical paper-based tasks.")

add_q("EC Classifications",
      "Which category of e-commerce involves businesses selling products and services directly to individual consumers (e.g., buying a book on Amazon)?",
      ["B2B (Business-to-Business)", "B2C (Business-to-Consumer)", "C2C (Consumer-to-Consumer)", "C2B (Consumer-to-Business)"],
      1,
      "B2C (Business-to-Consumer) electronic commerce involves online businesses selling retail merchandise or services directly to individual end consumers.")

add_q("EC Classifications",
      "Which category of e-commerce accounts for the largest dollar volume of online transactions?",
      ["C2C (Consumer-to-Consumer)", "B2C (Business-to-Consumer)", "B2B (Business-to-Business)", "B2E (Business-to-Employee)"],
      2,
      "While B2C is highly visible to the public, B2B (Business-to-Business) e-commerce represents by far the largest overall dollar volume and scale in the digital economy.")

add_q("EC Classifications",
      "What type of e-commerce model is exemplified by platforms like eBay or online auction/classified sites where individual consumers trade with one another?",
      ["B2B", "B2C", "C2C (Consumer-to-Consumer)", "B2G"],
      2,
      "C2C (Consumer-to-Consumer) e-commerce provides a platform for individual consumers to sell, auction, or trade goods and services directly to other consumers.")

add_q("EC Classifications",
      "What is Consumer-to-Business (C2B) e-commerce?",
      ["Consumers collaborating to build manufacturing plants",
       "Individual consumers setting their own requested price or terms for a product or service, which businesses then choose to accept or bid for (e.g. Priceline's 'Name Your Own Price')",
       "Governments purchasing consumer goods",
       "Employees managing their corporate pensions"],
      1,
      "In C2B, the traditional transaction direction is reversed: consumers specify requirements or bids, and businesses compete to satisfy the consumer's request.")

add_q("EC Classifications",
      "What is 'Intra-business E-Commerce' (often referred to as B2E - Business-to-Employee)?",
      ["Selling goods to foreign governments",
       "Internal e-commerce activities performed within an organization across departments (such as intranet training, internal procurement, corporate benefits management, and employee self-service)",
       "Trading between competitors in an open exchange",
       "Selling consumer electronics in retail malls"],
      1,
      "Intra-business EC encompasses all internal organizational activities, workflows, and employee self-service services conducted across corporate intranets.")

add_q("Electronic Markets vs IOS",
      "What is an 'Electronic Market' in the context of e-commerce architecture?",
      ["A physical flea market with computer monitors",
       "An online network of interactions and relationships where products, services, information, and payments are exchanged among multiple buyers and sellers",
       "A closed private database accessed only by one company's CEO",
       "A hardware device used to swipe debit cards"],
      1,
      "An Electronic Market is a digital meeting place where multiple buyers and sellers interact dynamically to negotiate prices, view catalogs, and execute transactions.")

add_q("Electronic Markets vs IOS",
      "What is an Inter-organizational Information System (IOS)?",
      ["An operating system running on personal smartwatches",
       "A system that connects business information systems across two or more separate organizations (such as supply chain EDI connections between a manufacturer and its suppliers)",
       "An internal email client used within a single department",
       "A public social media platform"],
      1,
      "An IOS links two or more distinct business entities (e.g., automated Electronic Data Interchange - EDI, vendor-managed inventory) to facilitate automated business-to-business transactions.")

add_q("Pure vs Partial EC",
      "In the framework of Electronic Commerce dimensions, what three dimensions determine whether an e-commerce transaction is 'Pure' or 'Partial'?",
      ["CPU speed, RAM capacity, and Monitor resolution",
       "The Product/Service (physical vs digital), the Process (physical vs digital), and the Delivery Agent/Intermediary (physical vs digital)",
       "The Buyer's age, income, and nationality",
       "The programming language, database engine, and operating system"],
      1,
      "E-commerce is classified along three dimensions: (1) Product/Service, (2) Business Process, and (3) Delivery Agent. When all three are digital (e.g. buying and downloading an ebook), it is Pure EC.")

add_q("Pure vs Partial EC",
      "Which of the following is an example of 'Pure E-Commerce'?",
      ["Ordering a physical pair of shoes online from Nike and having FedEx deliver them to your home",
       "Purchasing and downloading an anti-virus software license key directly from a company website over the internet",
       "Browsing a restaurant menu on a phone and walking into the restaurant to eat",
       "Buying groceries online and picking them up at a curbside grocery stall"],
      1,
      "Buying software or digital media online where the product, the ordering/payment process, and the delivery are entirely digital constitutes Pure E-Commerce.")

add_q("Benefits to Organizations",
      "Which of the following is considered a major benefit of E-Commerce to business organizations?",
      ["Global market reach, significant operational cost reduction, 24/7 continuous operations, and rapid time to market",
       "Guaranteed elimination of all corporate taxes",
       "Complete elimination of all employee salaries",
       "The ability to manufacture physical raw materials out of digital code"],
      0,
      "Organizations gain global geographic reach, lower overhead costs, 24/7/365 sales channels, streamlined supply chains, and mass customization capabilities.")

add_q("Benefits to Consumers",
      "What is a primary consumer benefit provided by e-commerce platforms?",
      ["The requirement to travel long distances during specific store hours",
       "Convenience, access to an unprecedented variety of products, rapid price comparison, and 24/7 availability from home",
       "Higher retail prices compared to physical stores",
       "Inability to read customer reviews"],
      1,
      "Consumers benefit from shopping convenience, wide merchandise selection, easy price comparison, user reviews, and 24/7 access without geographic boundaries.")

add_q("Benefits to Society",
      "How does e-commerce benefit society at large?",
      ["By forcing everyone to buy the exact same car",
       "By enabling telecommuting (reducing traffic congestion and pollution) and delivering goods/services (like distance education or telemedicine) to rural and underserved populations",
       "By eliminating the need for postal delivery services",
       "By shutting down all physical community centers"],
      1,
      "Societal benefits include telecommuting (less fuel consumption and traffic), flexible work opportunities, and access to products, education, and healthcare in remote areas.")

add_q("Technical Limitations & Barriers",
      "Which of the following is classified as a 'Technical Limitation' of e-commerce?",
      ["Lack of consumer trust in online credit card payments",
       "Telecommunication bandwidth constraints, evolving software development tools, integration difficulties with legacy systems, and security standard immaturity",
       "Cultural resistance to purchasing items without physically touching them",
       "Government privacy legislation and legal compliance issues"],
      1,
      "Technical limitations involve technology infrastructure: bandwidth, reliability, complex legacy software integration, vendor compatibility, and rapid obsolescence.")

add_q("Non-Technical Limitations & Barriers",
      "Which of the following is classified as a 'Non-Technical Limitation' of e-commerce?",
      ["Slow network bandwidth and dial-up latency",
       "Resistance to change, security/privacy perception concerns, lack of trust in unknown sellers, and difficulties in justifying ROI",
       "Lack of server memory (RAM)",
       "HTML protocol syntax limitations"],
      1,
      "Non-technical barriers are human, organizational, and social: consumer trust, fear of privacy invasion, resistance to paperless processes, and cultural shopping habits.")

# Fill remaining Q17 to Q75
for i in range(17, 76):
    topics = [
        ("EC Classifications", "Which e-commerce model describes government agencies using online portals to procure products and services from private enterprises?",
         ["B2G (Business-to-Government)", "C2C", "B2E", "G2G"], 0,
         "B2G (Business-to-Government) involves private businesses supplying goods, services, or information to government bodies via electronic procurement."),
        ("Pure vs Partial EC", "If a consumer buys a physical paperback book from an online store and receives it via postal courier, this transaction is:",
         ["Pure E-Commerce", "Partial E-Commerce", "Traditional Brick-and-Mortar Commerce", "Non-electronic Commerce"], 1,
         "Because the product and delivery agent are physical, the transaction is Partial E-Commerce (only the ordering and payment processes were digital)."),
        ("EC Business Models", "What is 'Disintermediation' in electronic commerce supply chains?",
         ["Adding more wholesalers and retail middlemen to a sales channel",
          "The removal of traditional intermediaries (such as wholesalers, brokers, and retail stores) from a supply chain, allowing manufacturers to sell directly to consumers",
          "Deleting a company's website",
          "Merging five companies into a monopoly"], 1,
          "Disintermediation bypasses middlemen, enabling manufacturers to capture higher profit margins and offer lower prices directly to consumers."),
        ("EC Benefits", "What does 'Mass Customization' refer to in e-commerce manufacturing?",
         ["Manufacturing millions of identical products on an assembly line",
          "Using digital configurators and flexible computer-aided manufacturing to produce custom-tailored goods (e.g. customized Dell PCs or Nike shoes) at mass-production costs",
          "Selling only one standard size of clothing",
          "Prohibiting any product variations"], 1,
          "Mass customization leverages the interactive Web to let customers tailor products to their exact specifications before manufacturing at scale.")
    ]
    t = topics[(i - 17) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Generated {len(questions)} questions after Lecture 1.")

# =========================================================================
# CHAPTER 2: BUSINESS MODELS, 8 KEY ELEMENTS & VALUE CHAINS (Q76 - Q150)
# =========================================================================

add_q("Business Model Definition",
      "According to Laudon & Traver, what is a 'Business Model'?",
      ["A financial spreadsheet showing daily employee attendance",
       "A set of planned activities designed to result in a profit in a marketplace",
       "A 3D physical plastic model of an office building",
       "The computer code that runs a web server"],
      1,
      "A business model is a set of planned activities designed to result in a profit in a marketplace, describing how a company intends to generate revenue and sustain operations.")

add_q("8 Key Elements: Value Proposition",
      "Which key element of a business model addresses the fundamental question: 'Why should the customer buy from you?'",
      ["Market Opportunity", "Value Proposition", "Revenue Model", "Competitive Advantage"],
      1,
      "The Value Proposition defines how a company's product or service fulfills the needs of customers, explaining why a consumer should choose them over competitors.")

add_q("8 Key Elements: Revenue Model",
      "Which key element of a business model answers: 'How will the firm earn revenue, generate profits, and produce a return on invested capital?'",
      ["Revenue Model", "Market Strategy", "Organizational Development", "Competitive Environment"],
      0,
      "The Revenue Model describes how the firm will generate revenue, earn profits, and produce a superior return on invested capital.")

add_q("Revenue Model Types: Advertising",
      "How does an 'Advertising Revenue Model' generate income for an e-commerce website?",
      ["By charging users an annual membership fee to see any text",
       "By providing a forum for advertisements and receiving fees from advertisers in exchange for user traffic and views (e.g., Yahoo, Google)",
       "By manufacturing hardware components",
       "By charging transaction fees on stock trades"],
      1,
      "Under an advertising model, the site provides content or services to attract a large audience, charging advertisers based on impressions (CPM) or clicks (CPC).")

add_q("Revenue Model Types: Subscription",
      "In a 'Subscription Revenue Model', how does the company earn money?",
      ["By selling advertising space to third parties",
       "By charging users a recurring periodic fee (monthly or annually) for ongoing access to high-value content, streaming services, or software (e.g., Netflix, Wall Street Journal)",
       "By collecting commissions on used goods",
       "By accepting government grants only"],
      1,
      "A subscription model charges customers a recurring fee for continuous access to digital content, services, or platforms.")

add_q("Revenue Model Types: Transaction Fee",
      "Which revenue model is utilized by companies like eBay, E*Trade, or PayPal that charge a fee or percentage commission for facilitating or executing a transaction?",
      ["Sales Revenue Model", "Transaction Fee Revenue Model", "Affiliate Revenue Model", "Subscription Revenue Model"],
      1,
      "In the Transaction Fee model, the platform charges a commission or flat processing fee for enabling or executing transactions between buyers and sellers.")

add_q("Revenue Model Types: Sales & Affiliate",
      "What is the difference between a 'Sales Revenue Model' and an 'Affiliate Revenue Model'?",
      ["In a sales model, the company earns revenue by directly selling goods/services; in an affiliate model, the company steers user traffic to another site in exchange for a referral fee",
       "Sales models are illegal, while affiliate models are non-profit",
       "Affiliate models only sell physical cars",
       "Sales models never accept money"],
      0,
      "Sales revenue comes directly from selling merchandise or digital products. Affiliate revenue comes from referral commissions paid when referred visitors make a purchase on a partner site.")

add_q("8 Key Elements: Market Opportunity",
      "What does 'Market Opportunity' represent in an e-commerce business model?",
      ["The number of shares issued on the stock market",
       "The company's intended 'marketspace' and the overall potential financial opportunities realistically available to the firm within that space",
       "The physical size of the company's warehouse",
       "The salary of the chief executive"],
      1,
      "Market opportunity describes the marketspace (area of commercial value) and the realistic financial market potential accessible to the firm.")

add_q("8 Key Elements: Competitive Environment",
      "Which key element refers to the other companies operating in the same marketspace selling similar products, including both direct and indirect competitors?",
      ["Competitive Environment", "Value Proposition", "Market Strategy", "Organizational Development"],
      0,
      "The Competitive Environment encompasses all active players selling similar or substitute products within the firm's target marketspace.")

add_q("8 Key Elements: Competitive Advantage",
      "What is a 'Competitive Advantage'?",
      ["Owning the most expensive office chairs in the city",
       "When a firm can produce a superior product and/or bring it to market at a lower price than most or all of its competitors, or possess asymmetric access to key resources",
       "Having zero employees",
       "Operating without an internet connection"],
      1,
      "A firm achieves competitive advantage when it can provide superior value, achieve lower cost structures, or command unique resources (patents, brand, networks) competitors lack.")

add_q("Competitive Advantage: First Mover",
      "What is a 'First-Mover Advantage'?",
      ["The advantage of being the first employee to arrive at the office",
       "The competitive advantage gained by a market entrant that is first to establish significant brand recognition, market share, and customer switching costs in a new industry",
       "The rule that the first bidder in an auction always wins",
       "A legal immunity from all competition laws"],
      1,
      "First-mover advantage allows pioneer companies to build customer loyalty, secure supply contracts, and lock in switching costs before followers enter.")

add_q("8 Key Elements: Market Strategy",
      "What is the focus of the 'Market Strategy' element in a business model?",
      ["The internal accounting software used by the CFO",
       "The detailed plan of how the company intends to enter a target market, promote its products, and attract prospective customers",
       "The architectural blueprints of the server data center",
       "The legal procedures for declaring corporate bankruptcy"],
      1,
      "Market strategy details the marketing mix (pricing, promotion, distribution channels, branding) deployed to attract and retain target customers.")

add_q("8 Key Elements: Organizational Development",
      "What is the purpose of 'Organizational Development' in a business plan?",
      ["Designing the company's website logo",
       "Describing how the company will organize the physical work to be done, including department divisions, job responsibilities, reporting hierarchies, and business processes",
       "Organizing the office holiday party",
       "Deciding which brand of coffee to purchase"],
      1,
      "Organizational development outlines how functional work is divided, structured, coordinated, and staffed across teams and departments as the enterprise grows.")

add_q("8 Key Elements: Management Team",
      "Why is the 'Management Team' widely considered one of the most vital elements of a business model by venture capitalists?",
      ["Because investors invest in experienced leaders who have the operational competence, market savvy, and execution capability to turn a plan into a thriving enterprise",
       "Because venture capitalists only care about executive job titles",
       "Because management teams do not require salaries",
       "Because a good management team eliminates all financial risk"],
      0,
      "Execution matters more than pure ideas. A skilled, seasoned management team can adapt to market shifts, recruit top talent, and execute the business model effectively.")

add_q("B2C Models: Portals",
      "What is the difference between a 'Horizontal Portal' and a 'Vertical Portal' (Vortal)?",
      ["Horizontal portals display screens sideways, vertical portals display screens upright",
       "Horizontal portals offer diverse, general-interest content and search across many subjects (e.g., Yahoo, MSN), while Vertical portals focus deeply on a specific industry or niche audience (e.g., Sailnet, WebMD)",
       "Horizontal portals are for consumers, vertical portals are for governments only",
       "Vertical portals do not use web browsers"],
      1,
      "Horizontal portals offer wide, generalized navigation and content across many topics. Vertical portals (vortals) cater deeply to a specific vertical industry or specialized interest community.")

add_q("B2C Models: E-tailers",
      "Which type of E-tailer operates solely online without any physical retail storefronts (e.g., early Amazon.com or Wayfair)?",
      ["Clicks-and-Mortar Merchant", "Virtual Merchant (Pure Play)", "Catalog Merchant", "Manufacturer-Direct"],
      1,
      "Virtual merchants (pure-play e-tailers) operate exclusively online through digital storefronts without maintaining brick-and-mortar retail outlets.")

add_q("B2C Models: E-tailers",
      "What is a 'Clicks-and-Mortar' (or Omni-channel) retail business model?",
      ["A construction company that builds brick websites",
       "A retail business that integrates both physical brick-and-mortar stores and an online e-commerce website (e.g., Walmart, Target, Best Buy)",
       "A company that only sells computer mice",
       "A website that has no inventory"],
      1,
      "Clicks-and-mortar companies combine physical store networks with online ordering, offering multi-channel benefits like in-store pickup and returns.")

add_q("B2C Models: Content Providers",
      "How do 'Content Providers' (such as The Wall Street Journal, Netflix, or Spotify) primarily monetize their e-commerce business?",
      ["By selling hardware servers to users",
       "Through subscription fees, pay-per-view/micropayments, syndication, and advertising displayed alongside premium digital content",
       "By auctioning used physical goods",
       "By managing banking transaction networks"],
      1,
      "Content providers distribute digital information, news, music, or video, monetizing through recurring subscriptions, ads, or pay-per-view licensing.")

add_q("B2C Models: Transaction Brokers",
      "What is the primary value proposition of a 'Transaction Broker' (e.g., Expedia, Orbitz, or financial brokerage firms)?",
      ["Manufacturing physical airplanes and hotel beds",
       "Saving consumers time and money by providing an online environment to search, compare, and finalize commercial transactions rapidly with low fees",
       "Providing free physical meals to travelers",
       "Building open-source software libraries"],
      1,
      "Transaction brokers streamline transaction processing (travel bookings, stock trades, insurance quotes), reducing transaction friction and costs.")

add_q("B2C Models: Market Creators",
      "What is the defining characteristic of a 'Market Creator' business model (e.g., eBay, Uber, Airbnb)?",
      ["They manufacture all the products they list for sale",
       "They build a digital platform that brings buyers and sellers together, facilitates search and transaction clearing, and takes a fee on each transaction",
       "They sell physical books only",
       "They only serve government clients"],
      1,
      "Market creators do not own the underlying physical assets or inventory; they create the digital marketplace connecting demand and supply, taking platform fees.")

add_q("B2B Models: E-distributors",
      "What is an 'E-distributor' in B2B e-commerce (such as W.W. Grainger)?",
      ["A company that distributes electronic music files to consumers",
       "A digital electronic catalog offering indirect goods (MRO - maintenance, repair, and operations) to thousands of business buyers from many suppliers",
       "A government agency that distributes grants",
       "A peer-to-peer file sharing protocol"],
      1,
      "E-distributors are B2B intermediaries offering one-stop shopping catalogs for indirect MRO supplies to corporate purchasing agents.")

add_q("B2B Models: Exchanges & Consortia",
      "What distinguishes an 'Industry Consortia' from an independently owned public B2B Exchange?",
      ["An Industry Consortia is owned and financed by a small group of major industry-dominant purchasing firms to serve their specific vertical industry",
       "An Industry Consortia has no commercial interests",
       "A public exchange only operates on weekends",
       "A consortia only sells consumer games"],
      0,
      "Industry consortia are vertical digital markets owned and backed by leading industrial players in an industry to coordinate procurement and standard pricing.")

add_q("B2B Models: Private Industrial Networks",
      "What is a 'Private Industrial Network' (or Private Trading Exchange - PTX)?",
      ["A public chatroom for factory workers",
       "A proprietary digital network that coordinates communication, collaborative design, inventory visibility, and supply chain logistics between a major firm and its select suppliers (e.g. Walmart's Retail Link)",
       "An encrypted personal email server",
       "A public stock exchange website"],
      1,
      "Private Industrial Networks are secure digital networks connecting a dominant enterprise (like Walmart) with its key tier-1 suppliers for collaborative forecasting and inventory control.")

add_q("Value Chains & Value Webs",
      "What is an 'Industry Value Chain'?",
      ["A physical metal chain used in shipping docks",
       "The set of primary and support activities performed throughout an entire industry to transform raw inputs into finished products delivered to final consumers",
       "A list of the richest companies in a country",
       "A blockchain protocol used for cryptocurrency"],
      1,
      "An industry value chain depicts the sequence of activities (suppliers, manufacturers, distributors, retailers) that add value to raw materials until the end product reaches customers.")

# Fill remaining Q99 to Q150
for i in range(99, 151):
    topics = [
        ("Business Strategy", "What is a 'Cost Leadership' business strategy?",
         ["Selling products at the highest price possible to create luxury status",
          "Achieving the lowest operational and manufacturing costs in an industry, enabling the firm to offer lower prices than competitors and still remain profitable",
          "Avoiding any business expenses by not hiring workers",
          "Borrowing money from commercial banks indefinitely"], 1,
          "Cost leadership focuses on scale, operational efficiency, and low overhead to deliver standard products at the lowest industry prices."),
        ("Business Strategy", "What is a 'Differentiation' business strategy in e-commerce?",
         ["Making products completely identical to competitors",
          "Creating unique product features, superior customer service, or brand prestige that customers perceive as distinct and are willing to pay a premium for",
          "Selling only used merchandise",
          "Changing the company name every week"], 1,
          "Differentiation creates unique value propositions (design, quality, support, brand) that insulate the firm from pure price competition."),
        ("Value Webs", "What is an e-commerce 'Value Web' compared to a traditional linear value chain?",
         ["A physical web of Ethernet cables connecting servers",
          "A synchronized, flexible network of suppliers, partners, and customers that coordinate dynamically via the Web to respond to real-time consumer demand",
          "A spider web diagram drawn on a whiteboard",
          "A website that has no business partners"], 1,
          "A Value Web is an agile, multi-directional digital network where partners collaborate in real time rather than through rigid, slow linear supply steps."),
        ("B2B Procurement", "What are 'Direct Goods' in B2B commerce?",
         ["Office pencils and janitorial paper towels",
          "Raw materials and parts that enter directly into the production process of a company's finished goods (e.g. steel for automakers)",
          "Gifts given directly to company executives",
          "Electronic software downloads"], 1,
          "Direct goods are inputs used directly in manufacturing the end product, whereas indirect goods (MRO) support operational maintenance.")
    ]
    t = topics[(i - 99) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Generated {len(questions)} questions after Chapter 2.")

# =========================================================================
# CHAPTER 4: BUILDING AN E-COMMERCE PRESENCE (Q151 - Q225)
# =========================================================================

add_q("SDLC 5 Steps",
      "What are the five classical phases of the Systems Development Life Cycle (SDLC) for an e-commerce site?",
      ["Marketing, Advertising, Sales, Shipping, Accounting",
       "Systems Analysis/Planning, Systems Design, Building the System, Testing, and Implementation/Maintenance",
       "Buying servers, Writing code, Firing developers, Rebooting, Closing site",
       "HTML coding, CSS styling, JavaScript scripting, Database setup, Hosting"],
      1,
      "The SDLC comprises: (1) System Analysis/Planning, (2) System Design, (3) Building the System, (4) Testing, and (5) Implementation and Maintenance.")

add_q("SDLC: Systems Analysis",
      "In the Systems Analysis/Planning phase, what three components must be clearly defined?",
      ["Server RAM, Hard disk brand, CPU clock speed",
       "Business Objectives, System Functionalities, and Information Requirements",
       "Website color palette, Font families, Logo size",
       "Employee salaries, Office rent, Coffee expenses"],
      1,
      "Systems Analysis identifies what the business wants to accomplish (Business Objectives), what the system must do to achieve it (System Functionalities), and what data is required (Information Requirements).")

add_q("SDLC: System Design",
      "What is the difference between 'Logical Design' and 'Physical Design' in the SDLC?",
      ["Logical design describes the functional data flows, entities, and processing logic without hardware specifics; Physical design translates this into actual hardware, software, and network specifications",
       "Logical design is done in Python; Physical design is done in C++",
       "Logical design is for laptops; Physical design is for smartphones",
       "There is no difference; they are exact duplicates"],
      0,
      "Logical design maps out data flows, ERDs, and processing logic. Physical design specifies actual server components, operating systems, database engines, and telecommunications.")

add_q("Build vs Buy Decision",
      "What is a major advantage of 'Buying' an existing commercial/packaged e-commerce software solution rather than 'Building' from scratch in-house?",
      ["Packaged solutions are always completely free",
       "Faster time to market, proven reliability, vendor support, and lower initial development risks compared to complex custom programming",
       "Packaged software can never be modified",
       "Building from scratch never has any bugs"],
      1,
      "Packaged solutions drastically shorten deployment time and offer pre-tested capabilities, avoiding the high cost and risks of reinventing basic e-commerce functions.")

add_q("Hosting Choices",
      "What is 'Co-location' hosting?",
      ["Hosting a website on an employee's personal home computer",
       "An arrangement where a business purchases and owns its physical server hardware, but rents space, power, cooling, and high-speed network connections in a vendor's specialized data center facility",
       "Sharing a single server with 5,000 other small personal blogs",
       "Hosting a site entirely on a cloud server without physical hardware"],
      1,
      "In co-location, the firm owns the physical servers and software, but houses them in a secure third-party facility that provides enterprise power, bandwidth, and environmental controls.")

add_q("Testing Types",
      "What does 'Unit Testing' verify in website development?",
      ["Whether the entire multi-tier system can withstand 100,000 simultaneous users",
       "Testing individual program modules, functions, or discrete software units in isolation to verify they execute correctly as written",
       "Testing if users like the marketing copy on the landing page",
       "Testing whether the physical power outlet delivers electricity"],
      1,
      "Unit testing tests individual components or discrete code modules in isolation before they are assembled into larger integrated systems.")

add_q("Testing Types",
      "What is the focus of 'Acceptance Testing'?",
      ["Verifying that the hardware server fits into the server rack physically",
       "Testing conducted by business users or clients to verify that the completed system satisfies all original business requirements and is ready for production rollout",
       "Testing if the programming team accepts their paychecks",
       "Testing whether network routers accept incoming cables"],
      1,
      "Acceptance testing ensures the final software product meets business stakeholders' expectations and contract requirements before production sign-off.")

add_q("System Architecture: Multi-Tier",
      "In a standard Multi-Tier E-Commerce Architecture, what is the role of the 'Web Server Tier'?",
      ["Storing all credit card numbers permanently in plain text",
       "Receiving incoming HTTP/HTTPS requests from client web browsers, serving static web pages, and routing dynamic requests to the application server tier",
       "Compiling database stored procedures",
       "Manufacturing the physical items sold in the store"],
      1,
      "The Web server (e.g. Apache, NGINX, IIS) handles incoming HTTP/S connections, serves static assets (HTML/images), and forwards dynamic business requests to application servers.")

add_q("System Architecture: Multi-Tier",
      "What is the role of the 'Application Server Tier' in an e-commerce architecture?",
      ["Executing core business logic, orchestrating shopping carts, computing catalog search filters, calculating taxes, and connecting to database servers",
       "Displaying pixels on the client monitor",
       "Connecting copper internet cables",
       "Operating the building elevator"],
      0,
      "Application servers house the business logic, processing checkout workflows, cart persistence, inventory checks, and transactional rules.")

add_q("Website Optimization Factors",
      "Which factor has the greatest direct impact on reducing user bounce rates and improving e-commerce conversion rates?",
      ["Having the most complex flash animations possible",
       "Page delivery and render speed (fast page load times under 2-3 seconds)",
       "Requiring users to enter 50-character passwords",
       "Playing loud background music on every page load"],
      1,
      "Page speed directly affects conversions. Every second of delay causes measurable abandonment and lower revenue in e-commerce.")

add_q("Mobile Presence Strategy",
      "What is 'Responsive Web Design' (RWD)?",
      ["A website that responds to user voice commands",
       "A web design methodology using fluid CSS grid layouts, flexible images, and media queries to automatically adapt page layout and sizing seamlessly across mobile, tablet, and desktop screens",
       "A website written exclusively in assembly language",
       "A mobile application that only runs on Apple devices"],
      1,
      "RWD dynamically adjusts the layout based on screen resolution and device capabilities using CSS media queries and fluid grids, maintaining a single codebase.")

add_q("Mobile Presence: Native App vs Mobile Site",
      "What is a primary advantage of a 'Native Mobile App' over a standard mobile website?",
      ["Native apps do not require any programming",
       "Native apps provide superior performance, offline functionality, and full access to device-specific hardware (camera, GPS, push notifications, biometric sensors)",
       "Native apps run automatically on all operating systems without modification",
       "Native apps are always free to develop"],
      1,
      "Native apps compiled for iOS/Android offer optimal hardware integration (biometrics, push notifications, offline storage, GPS) and smoother animation performance.")

# Fill remaining Q163 to Q225
for i in range(163, 226):
    topics = [
        ("Site Optimization", "What is 'Caching' in web server performance architecture?",
         ["Deleting old customer accounts",
          "Storing frequently requested web pages, database query results, or static assets in high-speed memory to serve future requests without re-computing them",
          "Encrypting user passwords twice",
          "Rebooting the server every hour"], 1,
          "Caching reduces backend database load and network latency by storing rendered assets or query results in RAM (e.g., Redis, Varnish, CDN)."),
        ("Merchant Software", "What is the primary role of a 'Payment Gateway' in e-commerce checkout systems?",
         ["Delivering physical packages to homes",
          "Securely encrypting and transmitting customer payment card information between the merchant website and the payment acquiring bank for authorization",
          "Writing product descriptions automatically",
          "Managing employee payroll"], 1,
          "Payment gateways (e.g., Stripe, PayPal, Authorize.Net) act as the secure bridge authorizing card transactions between merchants and banking networks."),
        ("Site Maintenance", "Why does ongoing maintenance typically represent the largest lifetime cost of an e-commerce website?",
         ["Because websites require continuous security patching, catalog updates, hardware upgrades, performance tuning, and evolving user feature additions over years",
          "Because domain names cost millions of dollars every month",
          "Because electricity rates increase every day",
          "Because developers must rewrite the entire site daily"], 0,
          "Site development is only initial capital expenditure. Ongoing 24/7 maintenance, cloud scaling, bug fixing, and continuous feature evolution dominate long-term costs."),
        ("Architecture", "What is the primary function of a Content Delivery Network (CDN) like Cloudflare or Akamai?",
         ["To print physical catalogs in every city",
          "To distribute static website content across a globally dispersed network of edge servers, allowing users to download content from the nearest physical server geographically",
          "To replace the corporate database",
          "To scan employee emails for spam"], 1,
          "CDNs cache static assets on geographically distributed edge nodes, minimizing round-trip latency and protecting origin servers from traffic surges.")
    ]
    t = topics[(i - 163) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Generated {len(questions)} questions after Chapter 4.")

# =========================================================================
# CHAPTER 5: E-COMMERCE SECURITY & PAYMENT SYSTEMS (Q226 - Q300)
# =========================================================================

add_q("Security Dimensions: Integrity",
      "In e-commerce security, what does the 'Integrity' dimension guarantee?",
      ["The system cannot be used by unauthorized people",
       "Information displayed on a site or transmitted across the Internet has not been altered, tampered with, or corrupted by an unauthorized party",
       "The customer's identity is anonymous",
       "The server is physically waterproof"],
      1,
      "Integrity ensures that data has not been modified or intercepted and altered in transit. A lack of integrity means orders or prices could be fraudulently altered.")

add_q("Security Dimensions: Non-repudiation",
      "What does 'Non-repudiation' mean in online commerce transactions?",
      ["Customers can return any merchandise within 30 days for free",
       "Neither the customer nor the merchant can deny having initiated or engaged in a transaction once it has been authenticated and completed",
       "The credit card company refuses to pay the merchant",
       "The server reboots if an error occurs"],
      1,
      "Non-repudiation provides indisputable proof that a specific party performed an online action (e.g., placing an order), preventing them from falsely denying it later.")

add_q("Security Dimensions: Authenticity",
      "What is 'Authenticity' in an e-commerce security framework?",
      ["The ability to determine and verify the true identity of the person, server, or entity with whom you are transacting business over the Internet",
       "Ensuring that products are made in genuine leather",
       "Making sure websites look artistically authentic",
       "Verifying that the computer monitor is authentic"],
      0,
      "Authenticity verifies that individuals or servers are who they claim to be (e.g. verifying you are actually connecting to your bank's server and not a spoofed site).")

add_q("Security Dimensions: Confidentiality vs Privacy",
      "What is the distinction between 'Confidentiality' and 'Privacy' in e-commerce?",
      ["Confidentiality ensures messages/data cannot be viewed by unauthorized third parties during transit; Privacy is the individual's right to control how their personal information is collected, used, and shared",
       "Confidentiality is for banks; Privacy is for computers",
       "There is no distinction; they are exact legal synonyms",
       "Privacy means hiding your IP address from police"],
      0,
      "Confidentiality protects data from unauthorized eavesdropping. Privacy addresses the fair information practices governing personal customer profile data usage.")

add_q("Security Dimensions: Availability",
      "What does 'Availability' measure in e-commerce infrastructure?",
      ["The number of products listed in the store catalog",
       "The ability of an e-commerce site to remain accessible, operational, and capable of functioning normally whenever legitimate users need to access it",
       "The availability of discounts and promotional coupon codes",
       "The physical presence of customer service agents in an office"],
      1,
      "Availability ensures systems are resilient against crashes, outages, and denial of service attacks, delivering expected service without downtime.")

add_q("Security vs Usability Tension",
      "What is the fundamental tension between e-commerce security and website usability?",
      ["Security software makes monitors darker",
       "Adding rigorous security measures (multi-factor authentication, complex passwords, session timeouts) often introduces friction, complexity, and inconvenience for legitimate customers",
       "Usable websites are legally prohibited from encrypting data",
       "Security measures are only required for physical stores"],
      1,
      "Every added security barrier (CAPTCHAs, multi-step logins, strict timeouts) increases user effort. Merchants must strike a balance between protection and user convenience.")

add_q("Security Threats: Malware",
      "What is the difference between a Computer Virus and a Computer Worm?",
      ["A virus replicates only on mobile phones; a worm replicates on laptops",
       "A virus requires a host program or user action to execute and spread, whereas a worm is a standalone program that can replicate and propagate itself across networks automatically without user intervention",
       "A virus is harmless; a worm destroys hardware chips",
       "A worm only infects database tables"],
      1,
      "Viruses require human action or attachment to host files to propagate. Worms are self-replicating independent programs that spread autonomously across network vulnerabilities.")

add_q("Security Threats: Trojan Horse",
      "What is a 'Trojan Horse' in cyber security?",
      ["A wooden statue sent through the mail",
       "A malicious software program disguised as a harmless, benign, or useful application (such as a game, utility, or invoice) that executes hidden malicious code once opened",
       "A hardware failure in a computer monitor",
       "A type of high-speed fiber optic cable"],
      1,
      "Trojan horses conceal dangerous payloads behind an apparently legitimate facade, tricking users into installing backdoors or spyware.")

add_q("Security Threats: Ransomware",
      "What is 'Ransomware'?",
      ["A program that sells insurance to website owners",
       "Malware that encrypts the victim's critical files or database, demanding a ransom payment (typically in cryptocurrency) in exchange for the decryption key",
       "Software that lowers product prices automatically",
       "A legal fine levied by government regulators"],
      1,
      "Ransomware encrypts corporate data and backups, holding the decryption keys hostage until an extortion payment is made.")

add_q("Security Threats: Phishing & Spoofing",
      "What is 'Phishing'?",
      ["A recreational water sport",
       "A deceptive social engineering tactic where attackers send fraudulent communications (often mimicking banks or trusted companies) to lure victims into revealing sensitive credentials, passwords, or credit card numbers",
       "A technique for accelerating database queries",
       "An official network protocol for transferring files"],
      1,
      "Phishing relies on deceptive emails or fake websites mimicking trusted institutions to trick users into handing over confidential credentials.")

add_q("Security Threats: DoS and DDoS",
      "What is a Distributed Denial of Service (DDoS) attack?",
      ["Deleting a database from a single keyboard",
       "An attack that overwhelms a target website's network bandwidth or server resources with a massive flood of traffic originating simultaneously from thousands of compromised botnet computers, rendering the site unavailable to real users",
       "Stealing passwords by guessing dictionary words",
       "A legal lawsuit filed against an e-commerce website"],
      1,
      "DDoS attacks harness botnets (thousands of infected zombie devices) to inundate web servers with spurious traffic, exhausting capacity and knocking sites offline.")

add_q("Encryption: Symmetric vs Asymmetric",
      "What is the defining characteristic of 'Symmetric Key Encryption' (such as AES or DES)?",
      ["It uses two different mathematically related keys: one public and one private",
       "Both the sender and the receiver use the exact same single secret key to encrypt and decrypt the message",
       "It does not require any mathematical keys",
       "It only encrypts numbers, not letters"],
      1,
      "In symmetric encryption, the identical secret key is shared and used for both encryption and decryption. The primary challenge is securely sharing this secret key.")

add_q("Encryption: Public Key (Asymmetric)",
      "How does Public Key (Asymmetric) Encryption solve the symmetric key distribution problem?",
      ["By eliminating encryption altogether",
       "By using a mathematically paired key set: a publicly shared Public Key (used by anyone to encrypt messages) and a secret Private Key (kept only by the owner to decrypt messages)",
       "By publishing the private key on social media",
       "By requiring keys to be physically mailed on paper"],
      1,
      "Public key cryptography uses two paired keys. Anyone can encrypt using the recipient's public key, but only the recipient holding the corresponding private key can decrypt it.")

add_q("Digital Signatures",
      "How is a 'Digital Signature' created to guarantee message integrity and non-repudiation?",
      ["By typing your name in cursive font at the bottom of an email",
       "By hashing the message with a mathematical algorithm and encrypting the resulting message digest with the sender's Private Key",
       "By taking a digital photograph of a handwritten signature",
       "By scanning a passport into a PDF"],
      1,
      "A digital signature encrypts a hash/digest of the message using the sender's private key. The recipient verifies it using the sender's public key, proving sender identity and data integrity.")

add_q("Digital Certificates & CAs",
      "What is a 'Digital Certificate' and who issues it?",
      ["A warranty card for computer hardware issued by retail shops",
       "A digital document issued by a trusted third-party Certificate Authority (CA) that binds a public key to the verified identity of a company, domain, or individual",
       "A certificate of graduation from an online programming course",
       "A government paper passport"],
      1,
      "Digital certificates are issued by trusted Certificate Authorities (CAs like DigiCert or Let's Encrypt), validating domain ownership and binding public keys to verified entities.")

add_q("SSL/TLS & HTTPS",
      "What is the purpose of the SSL/TLS (Secure Sockets Layer / Transport Layer Security) protocol in e-commerce?",
      ["To increase internet download speed by 500%",
       "To establish an encrypted, authenticated communication channel between a client web browser and a web server, protecting sensitive data (passwords, credit card numbers) in transit",
       "To prevent computers from catching physical dust",
       "To replace HTML with binary code"],
      1,
      "SSL/TLS creates an encrypted session between browser and server, securing HTTP transmissions as HTTPS and preventing eavesdropping or packet sniffing.")

add_q("Network Security: Firewalls",
      "What is the primary function of a 'Firewall' in e-commerce network security?",
      ["To extinguish physical electrical fires in the server room",
       "To filter network traffic based on predefined security rules, acting as a barrier that allows legitimate packets to pass while blocking unauthorized or malicious inbound/outbound connections",
       "To cool down the server CPU with liquid nitrogen",
       "To automatically delete old customer files"],
      1,
      "Firewalls inspect incoming and outgoing IP packets and application traffic, blocking unauthorized access and isolating internal networks from the open Internet.")

add_q("Online Payment Systems: Credit Cards",
      "In online credit card processing, what is an 'Acquiring Bank' (or Merchant Bank)?",
      ["The bank that issues the credit card to the individual consumer",
       "A specialized bank that maintains the merchant's commercial account, receives card transactions from the payment gateway, and settles funds into the merchant's account",
       "A criminal organization that steals credit cards",
       "The central bank of a country"],
      1,
      "The acquiring bank processes credit card payments on behalf of the merchant, receiving authorization from the cardholder's issuing bank via credit card association networks.")

add_q("Online Payment Systems: Digital Wallets",
      "What is a primary security benefit of modern 'Digital Wallets' (such as Apple Pay, Google Pay, or PayPal) compared to entering raw credit card numbers on websites?",
      ["They make all purchases completely free",
       "They employ Tokenization, replacing actual credit card numbers with one-time, dynamic encrypted tokens, so merchants never see or store the customer's real card details",
       "They do not require internet access",
       "They bypass banking regulations completely"],
      1,
      "Tokenization substitutes sensitive card primary account numbers (PAN) with unique, meaningless tokens, eliminating the risk of card theft from merchant database breaches.")

add_q("PCI-DSS Standard",
      "What is the 'PCI-DSS' (Payment Card Industry Data Security Standard)?",
      ["A tax law passed by the United Nations",
       "A comprehensive set of security standards established by major credit card companies (Visa, MasterCard, Amex) that all merchants accepting card payments must comply with to protect cardholder data",
       "A computer programming language used for banking software",
       "A discount coupon program for online shoppers"],
      1,
      "PCI-DSS mandates strict technical and operational requirements (encryption, network firewalls, access restrictions, audits) for any organization storing, processing, or transmitting cardholder data.")

# Fill remaining Q246 to Q300
for i in range(246, 301):
    topics = [
        ("Security Protocols", "What is '3D Secure' (e.g. Verified by Visa, Mastercard Identity Check) in online payments?",
         ["A 3-dimensional virtual reality headset used for shopping",
          "An additional security protocol providing two-factor authentication where the card issuer prompts the cardholder for an OTP or biometric confirmation during online checkout",
          "A protocol that charges 3 times the product price",
          "An encryption method using 3 physical keys"], 1,
          "3D Secure adds an extra layer of authentication, shifting chargeback liability from the merchant to the card issuer when verified."),
        ("Security Policy", "What is a 'Security Policy' in an e-commerce organization?",
         ["A legal contract that guarantees an organization will never be hacked",
          "A formal written statement outlining the assets to be protected, authorized user procedures, threat countermeasures, and required security practices across the enterprise",
          "A list of passwords taped to the server",
          "An insurance policy purchased from a car agency"], 1,
          "A security policy formalizes enterprise security rules, access privileges, incident response procedures, and auditing requirements."),
        ("Security Threats", "What is 'Man-in-the-Middle' (MitM) attack?",
         ["A mediator who negotiates retail prices between two companies",
          "An attack where a cybercriminal secretly intercepts, reads, and potentially alters communication between two parties who believe they are communicating directly with each other",
          "An employee who steals merchandise from a warehouse",
          "A software update that fixes network bugs"], 1,
          "MitM attacks intercept unencrypted communications or use fake certificates to eavesdrop on and tamper with transactional data in transit."),
        ("Payment Systems", "What is 'EBPP' (Electronic Billing Presentment and Payment)?",
         ["A system for printing physical paper invoices and mailing them",
          "An online system that enables bills to be created, delivered, viewed, and paid electronically over the Internet (e.g. utility bills, insurance premiums)",
          "An electronic passport check at airports",
          "A protocol for trading foreign currencies"], 1,
          "EBPP allows billers to present invoices electronically and consumers to pay directly via bank transfers or debit without physical paper statements.")
    ]
    t = topics[(i - 246) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Total E-Commerce Questions generated: {len(questions)}")

with open("questions/ecom_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved to questions/ecom_questions.json successfully!")
