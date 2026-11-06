# scripts/build_batch3.py
# Questions 101 to 150: Online Security and Payment Systems (Doc 3)

questions_batch3 = [
    {
        "id": "ecom_101",
        "subject": "E-Commerce",
        "topic": "Security Dimensions: Integrity",
        "question": "Which dimension of e-commerce security ensures that information transmitted across the Internet has not been altered or tampered with?",
        "options": [
            "Data nonrepudiation",
            "System availability",
            "Message integrity",
            "Entity authenticity"
        ],
        "answer": 2,
        "explanation": "Integrity refers to the ability to ensure that information displayed on a website or transmitted over the Internet has not been altered by an unauthorized party."
    },
    {
        "id": "ecom_102",
        "subject": "E-Commerce",
        "topic": "Security Dimensions: Non-repudiation",
        "question": "A customer places an online stock order and later attempts to cancel it by claiming someone else sent the transaction. Which security dimension prevents this?",
        "options": [
            "Information confidentiality",
            "Transaction nonrepudiation",
            "Application availability",
            "Platform scalability"
        ],
        "answer": 1,
        "explanation": "Nonrepudiation refers to the ability to ensure that e-commerce participants cannot deny having engaged in an online transaction or sent a message."
    },
    {
        "id": "ecom_103",
        "subject": "E-Commerce",
        "topic": "Security Dimensions: Authenticity",
        "question": "What does the authenticity dimension of e-commerce security specifically verify for transacting parties?",
        "options": [
            "Confirming the true identity of the person or business entity you are dealing with online",
            "Guaranteeing that web server hardware microprocessors operate at rated clock speeds",
            "Ensuring that delivered physical parcels are delivered within twenty-four hours of ordering",
            "Prohibiting corporate networks from maintaining historical customer transaction logs"
        ],
        "answer": 0,
        "explanation": "Authenticity refers to the ability to identify and verify the real identity of a person, firm, or computer system with whom an online transaction is conducted."
    },
    {
        "id": "ecom_104",
        "subject": "E-Commerce",
        "topic": "Security Dimensions: Confidentiality vs Privacy",
        "question": "How does confidentiality differ from privacy within the e-commerce security framework?",
        "options": [
            "Confidentiality shields messages from unauthorized interception; privacy controls personal data usage",
            "Confidentiality applies only to email; privacy applies only to credit card account numbers",
            "Privacy ensures systems remain online 24/7; confidentiality prevents hardware equipment failures",
            "Confidentiality is managed by public laws; privacy is enforced exclusively through network routers"
        ],
        "answer": 0,
        "explanation": "Confidentiality ensures messages and data are accessible only to authorized persons, while privacy focuses on an individual's right to control how personal data is collected and used."
    },
    {
        "id": "ecom_105",
        "subject": "E-Commerce",
        "topic": "Security Dimensions: Availability",
        "question": "A merchant's online catalog becomes completely unreachable during a major holiday shopping event due to a cyberattack. Which dimension is breached?",
        "options": [
            "Authenticity",
            "Availability",
            "Nonrepudiation",
            "Confidentiality"
        ],
        "answer": 1,
        "explanation": "Availability refers to the ability to ensure that an e-commerce website, servers, and networks continue to function and remain accessible as intended."
    },
    {
        "id": "ecom_106",
        "subject": "E-Commerce",
        "topic": "Security Environment & Trade-offs",
        "question": "What is the recognized operational tension between e-commerce security and website ease of use?",
        "options": [
            "Implementing extensive security controls often makes sites more cumbersome and slower for consumers",
            "Adding security mechanisms automatically doubles consumer broadband connection transmission speeds",
            "Consumers consistently refuse to browse websites that display valid digital security certificates",
            "Federal banking regulations prohibit encrypted websites from displaying commercial merchandise photos"
        ],
        "answer": 0,
        "explanation": "There is a direct tension between security and usability: the more security measures added, the more difficult a site is to navigate and the slower transactions can become."
    },
    {
        "id": "ecom_107",
        "subject": "E-Commerce",
        "topic": "Security Environment & Trade-offs",
        "question": "What are the three primary points of vulnerability in a typical e-commerce transaction environment?",
        "options": [
            "The client workstation, the communications pipeline, and the merchant web server",
            "The physical product warehouse, the assembly line, and the corporate boardroom",
            "The local electrical power grid, the postal carrier van, and the paper checkbook",
            "The marketing advertising agency, the print media catalog, and the retail storefront"
        ],
        "answer": 0,
        "explanation": "The three primary vulnerability points in an e-commerce environment are the client computer, the server hosting the site, and the communications pipeline connecting them."
    },
    {
        "id": "ecom_108",
        "subject": "E-Commerce",
        "topic": "Security Threats: Malware",
        "question": "How does a computer worm fundamentally differ from a standard computer virus?",
        "options": [
            "A worm replicates across networks independently without needing to attach to a host file",
            "A worm can only execute on mainframe computers and cannot infect personal workstations",
            "A virus spreads exclusively through physical optical laser cables between data centers",
            "A virus is harmless marketing software whereas a worm permanently destroys server hardware"
        ],
        "answer": 0,
        "explanation": "A virus must attach itself to an executable program or document to spread, whereas a worm is standalone software designed to spread automatically across networks."
    },
    {
        "id": "ecom_109",
        "subject": "E-Commerce",
        "topic": "Security Threats: Malware",
        "question": "A user downloads a free system utility that appears harmless, but secretly installs an unauthorized backdoor allowing remote hackers access. This is a:",
        "options": [
            "Trojan horse program",
            "Browser cookie tracker",
            "Hardware packet filter",
            "Cryptographic hash digest"
        ],
        "answer": 0,
        "explanation": "A Trojan horse appears to perform a benign or useful function, but secretly harbors a hidden malicious payload such as a backdoor."
    },
    {
        "id": "ecom_110",
        "subject": "E-Commerce",
        "topic": "Security Threats: Malware",
        "question": "What is a 'botnet' in the context of global e-commerce cybersecurity threats?",
        "options": [
            "A network of compromised computers controlled remotely by a hacker to launch attacks",
            "An authorized consortium of banking servers managing international currency settlements",
            "A hardware device used by Internet service providers to boost optical signal strengths",
            "A search engine indexing crawler designed to discover discounted retail merchandise"
        ],
        "answer": 0,
        "explanation": "A botnet is a collection of compromised computers ('zombies') infected with malware and controlled remotely by an attacker to execute coordinated cybercrimes."
    },
    {
        "id": "ecom_111",
        "subject": "E-Commerce",
        "topic": "Security Threats: Unwanted Programs",
        "question": "Which category of unwanted program covertly records a user's keystrokes, passwords, and sensitive browsing habits?",
        "options": [
            "Spyware",
            "Packet sniffers",
            "Application gateways",
            "Digital certificates"
        ],
        "answer": 0,
        "explanation": "Spyware is software covertly installed on a computer to monitor user actions, keystrokes, passwords, and personal information, transmitting data to an unauthorized third party."
    },
    {
        "id": "ecom_112",
        "subject": "E-Commerce",
        "topic": "Security Threats: Phishing & Spoofing",
        "question": "An email deceptively claiming to originate from a major bank directs recipients to a fraudulent login page to harvest account credentials. This attack is:",
        "options": [
            "Phishing attack",
            "Packet sniffing",
            "Symmetric hashing",
            "Buffer overflow"
        ],
        "answer": 0,
        "explanation": "Phishing is a deceptive online attempt to obtain confidential credentials using social engineering, fraudulent emails, and spoofed websites."
    },
    {
        "id": "ecom_113",
        "subject": "E-Commerce",
        "topic": "Security Threats: Phishing & Spoofing",
        "question": "How does 'pharming' differ from traditional email phishing attacks?",
        "options": [
            "Pharming automatically redirects user web browser requests by poisoning DNS tables or links",
            "Pharming targets only corporate mainframe databases rather than consumer computers",
            "Pharming requires physical access to a user's office keyboard and monitor hardware",
            "Pharming is an authorized testing technique conducted exclusively by certified ethical hackers"
        ],
        "answer": 0,
        "explanation": "Pharming involves spoofing a website by redirecting a legitimate URL or poisoning domain name resolution (DNS), steering users to a fake site even if they typed the correct address."
    },
    {
        "id": "ecom_114",
        "subject": "E-Commerce",
        "topic": "Security Threats: Hacking",
        "question": "Intentionally disrupting, altering, defacing, or destroying a commercial corporate website is technically termed:",
        "options": [
            "Cybervandalism",
            "Reverse proxying",
            "Asymmetric routing",
            "Packet filtering"
        ],
        "answer": 0,
        "explanation": "Cybervandalism is the intentional disruption, defacement, or destruction of a website or corporate digital asset."
    },
    {
        "id": "ecom_115",
        "subject": "E-Commerce",
        "topic": "Security Threats: Hacking",
        "question": "What differentiates a 'white hat' hacker from a 'black hat' hacker in cybersecurity practice?",
        "options": [
            "White hats are ethical security professionals authorized to discover and remediate vulnerabilities",
            "White hats develop malicious code while black hats create commercial antivirus software updates",
            "White hats operate exclusively on government networks while black hats target private merchants",
            "White hats use symmetric encryption whereas black hats rely entirely on asymmetric public keys"
        ],
        "answer": 0,
        "explanation": "White hats are authorized ethical hackers who identify security flaws to help organizations strengthen their defenses, whereas black hats act with malicious or criminal intent."
    },
    {
        "id": "ecom_116",
        "subject": "E-Commerce",
        "topic": "Security Threats: DoS and DDoS",
        "question": "How does a Distributed Denial of Service (DDoS) attack disable a targeted e-commerce website?",
        "options": [
            "By coordinating multiple compromised computers to flood the target server with useless traffic",
            "By decrypting and publishing the private keys of the merchant's digital certificate authority",
            "By physically cutting the undersea fiber-optic cables servicing the merchant's hosting facility",
            "By altering product database prices to zero through SQL injection attacks on shopping carts"
        ],
        "answer": 0,
        "explanation": "A DDoS attack uses numerous distributed compromised systems (often botnets) to overwhelm a target network or server with useless requests, exhausting bandwidth and system resources."
    },
    {
        "id": "ecom_117",
        "subject": "E-Commerce",
        "topic": "Security Threats: Sniffing & Insiders",
        "question": "What is a 'packet sniffer' program primarily used for in the context of network vulnerabilities?",
        "options": [
            "Eavesdropping on and intercepting unencrypted data packets as they travel across a network",
            "Compressing video streams to improve mobile device streaming performance across 3G networks",
            "Generating randomized public and private key pairs for certification authority servers",
            "Converting static HTML web pages into dynamic server-side Active Server Page scripts"
        ],
        "answer": 0,
        "explanation": "A sniffer is an eavesdropping software program that monitors and captures information traveling over a computer network, allowing eavesdroppers to read unencrypted data."
    },
    {
        "id": "ecom_118",
        "subject": "E-Commerce",
        "topic": "Security Threats: Sniffing & Insiders",
        "question": "According to industry cybersecurity studies, what constitutes the single largest financial threat to corporate information security?",
        "options": [
            "Insider jobs and unauthorized conduct committed by trusted employees",
            "Foreign teenage hackers launching sporadic cybervandalism defacements",
            "Accidental electrical failures occurring at third-party web hosting data centers",
            "Hardware defects occurring inside commercial off-the-shelf firewall routers"
        ],
        "answer": 0,
        "explanation": "Insider jobs—attacks or intellectual property theft executed by current or former employees with trusted access—represent the single largest source of financial losses in cybercrime."
    },
    {
        "id": "ecom_119",
        "subject": "E-Commerce",
        "topic": "Encryption: Fundamentals",
        "question": "Which of the six core dimensions of e-commerce security does encryption directly support?",
        "options": [
            "System availability, network scalability, hardware reliability, and ease of use",
            "Message integrity, nonrepudiation, entity authentication, and data confidentiality",
            "Price discrimination, automated procurement, search engine ranking, and bandwidth",
            "Social equity, cash convertibility, payment immediacy, and customer personalization"
        ],
        "answer": 1,
        "explanation": "Encryption directly provides 4 of the 6 key dimensions of e-commerce security: message integrity, nonrepudiation, authentication, and confidentiality."
    },
    {
        "id": "ecom_120",
        "subject": "E-Commerce",
        "topic": "Encryption: Symmetric Key",
        "question": "In symmetric key cryptography, how are encryption and decryption keys managed by transacting parties?",
        "options": [
            "Both sender and receiver must utilize the exact same secret digital key for both operations",
            "The sender uses a public key while the receiver uses a completely unrelated private password",
            "The keys are generated dynamically by public search engines without user intervention",
            "The sender publishes the secret key openly on a public bulletin board before transmission"
        ],
        "answer": 0,
        "explanation": "In symmetric key encryption, the sender and receiver share and use the exact same digital secret key to both encrypt and decrypt the transmitted message."
    },
    {
        "id": "ecom_121",
        "subject": "E-Commerce",
        "topic": "Encryption: Symmetric Key",
        "question": "Which symmetric cipher standard is currently the most widely deployed across commercial e-commerce systems?",
        "options": [
            "Data Encryption Standard (DES)",
            "Advanced Encryption Standard (AES)",
            "Rivest-Shamir-Adleman (RSA)",
            "Secure Hash Algorithm (SHA-1)"
        ],
        "answer": 1,
        "explanation": "The Advanced Encryption Standard (AES) is the most widely used symmetric encryption standard, commonly utilizing 128-, 192-, or 256-bit encryption keys."
    },
    {
        "id": "ecom_122",
        "subject": "E-Commerce",
        "topic": "Encryption: Symmetric Key",
        "question": "What is the primary operational weakness inherent to pure symmetric key encryption over public networks?",
        "options": [
            "The algorithm is too computationally slow to encrypt short electronic payment messages",
            "The secret key must be transmitted across insecure channels to the recipient in advance",
            "The cipher cannot be processed by computers using standard commercial microprocessors",
            "The encryption process permanently deletes the underlying plaintext data files"
        ],
        "answer": 1,
        "explanation": "The major weakness of symmetric key encryption is key distribution: securely sharing the shared secret key between parties over insecure public communication lines."
    },
    {
        "id": "ecom_123",
        "subject": "E-Commerce",
        "topic": "Encryption: Public Key",
        "question": "How does public key (asymmetric) cryptography solve the key distribution problem of symmetric encryption?",
        "options": [
            "By using two mathematically related keys: a widely disseminated public key and a private key",
            "By requiring both transacting parties to meet physically to exchange printed keycards",
            "By eliminating the need for mathematical keys and relying strictly on browser cookies",
            "By mandating that all transmitted messages be broadcast unencrypted over open lines"
        ],
        "answer": 0,
        "explanation": "Public key encryption uses a mathematically related key pair: a public key that can be openly distributed and a private key kept strictly confidential by the recipient."
    },
    {
        "id": "ecom_124",
        "subject": "E-Commerce",
        "topic": "Encryption: Public Key",
        "question": "When Alice sends an encrypted confidential message to Bob using public key cryptography, which key does Alice use?",
        "options": [
            "Bob's public key",
            "Alice's private key",
            "Bob's private key",
            "A public key from the CA"
        ],
        "answer": 0,
        "explanation": "To ensure confidentiality, Alice encrypts the message using Bob's public key. Only Bob's corresponding private key can decrypt the ciphertext."
    },
    {
        "id": "ecom_125",
        "subject": "E-Commerce",
        "topic": "Hash Functions & Digests",
        "question": "What is the primary function of a cryptographic hash algorithm (e.g., MD5 or SHA) in message transmission?",
        "options": [
            "Transforming variable-length input data into a unique, fixed-length digest to verify integrity",
            "Compressing high-definition video files so they stream smoothly over low-bandwidth connections",
            "Translating foreign-language web catalog descriptions into standardized domestic currencies",
            "Establishing physical circuit connections between client modems and telephone switches"
        ],
        "answer": 0,
        "explanation": "A hash function is a mathematical algorithm that produces a fixed-length numerical value (hash digest); any change to the source message alters the digest, proving tampering."
    },
    {
        "id": "ecom_126",
        "subject": "E-Commerce",
        "topic": "Digital Signatures",
        "question": "How is a digital signature created by a message sender using public key cryptography?",
        "options": [
            "By encrypting the message hash digest using the sender's own private key",
            "By typing the sender's legal full name at the bottom of an unencrypted text message",
            "By scanning an image of a physical handwritten signature into an email attachment",
            "By encrypting the entire document using the recipient's public key certificate"
        ],
        "answer": 0,
        "explanation": "A digital signature is created by computing a hash digest of the message and encrypting that digest with the sender's private key, providing authenticity and nonrepudiation."
    },
    {
        "id": "ecom_127",
        "subject": "E-Commerce",
        "topic": "Digital Envelopes",
        "question": "How does a 'digital envelope' combine symmetric and public key encryption to optimize performance?",
        "options": [
            "It encrypts the document with a fast symmetric key, and encrypts that symmetric key with the recipient's public key",
            "It transmits data packets inside physical sealed envelopes using registered commercial courier carriers",
            "It uses public key cryptography to encrypt massive video files and symmetric keys for short email headers",
            "It disables all network firewalls during transaction transmission to increase raw data throughput"
        ],
        "answer": 0,
        "explanation": "A digital envelope uses fast symmetric encryption to encrypt large documents, and uses slower public key encryption only to securely transmit the single symmetric key."
    },
    {
        "id": "ecom_128",
        "subject": "E-Commerce",
        "topic": "Digital Certificates & PKI",
        "question": "What is the fundamental role of a Certification Authority (CA) in a Public Key Infrastructure (PKI)?",
        "options": [
            "Issuing signed digital certificates that bind an individual or organization to their public key",
            "Processing credit card chargebacks when online consumers dispute merchandise purchases",
            "Auditing physical warehouse inventories for large B2C electronic retail enterprises",
            "Regulating international maritime tariff rates on imported computer microprocessor chips"
        ],
        "answer": 0,
        "explanation": "A Certification Authority (CA) is a trusted third-party organization that issues digital certificates verifying the identity of the certificate owner and validating their public key."
    },
    {
        "id": "ecom_129",
        "subject": "E-Commerce",
        "topic": "Securing Channels: SSL/TLS",
        "question": "What occurs during the initial negotiation phase when a client browser establishes an SSL/TLS session with a secure server?",
        "options": [
            "The client and server authenticate each other and negotiate a shared session key to encrypt the URL and content",
            "The server downloads all customer desktop personal files to an internal corporate archive database",
            "The client computer disables local operating system security patches to increase processing speed",
            "The merchant server charges the customer's credit card an initial non-refundable connection deposit"
        ],
        "answer": 0,
        "explanation": "SSL/TLS establishes a secure negotiated client-server session in which the server (and optionally client) authenticates and negotiates encryption keys, securing the URL and payload."
    },
    {
        "id": "ecom_130",
        "subject": "E-Commerce",
        "topic": "Securing Channels: S-HTTP",
        "question": "How does Secure HTTP (S-HTTP) conceptually differ from Secure Sockets Layer (SSL)?",
        "options": [
            "S-HTTP secures individual messages rather than establishing an entire encrypted transport session",
            "S-HTTP operates exclusively across private corporate intranets and cannot access the Internet",
            "S-HTTP does not support any cryptographic algorithms or digital certificate verification",
            "S-HTTP replaces standard web browsers with command-line database administrative shells"
        ],
        "answer": 0,
        "explanation": "While SSL secures the entire transport session (encrypting all communications between client and server), S-HTTP is designed to secure individual HTTP messages."
    },
    {
        "id": "ecom_131",
        "subject": "E-Commerce",
        "topic": "Securing Channels: VPNs",
        "question": "A remote telecommuting employee uses a Virtual Private Network (VPN) to access corporate files. What protocol is commonly used?",
        "options": [
            "Point-to-Point Tunneling Protocol (PPTP)",
            "Simple Mail Transfer Protocol (SMTP)",
            "Common Gateway Interface (CGI)",
            "Dynamic Host Configuration Protocol (DHCP)"
        ],
        "answer": 0,
        "explanation": "VPNs allow remote users to securely access internal networks via the public Internet using tunneling protocols like the Point-to-Point Tunneling Protocol (PPTP)."
    },
    {
        "id": "ecom_132",
        "subject": "E-Commerce",
        "topic": "Protecting Networks: Firewalls",
        "question": "How does a packet-filtering firewall determine whether network data packets are permitted to cross a perimeter?",
        "options": [
            "By examining packet header data including source IP, destination IP, and port numbers against rules",
            "By analyzing the emotional sentiment expressed within the text content of user email messages",
            "By physically weighing optical network switches to detect electronic data congestion",
            "By verifying whether the sending user possesses an active corporate credit card account"
        ],
        "answer": 0,
        "explanation": "Packet-filtering firewalls filter traffic by examining packet headers (IP addresses, protocol types, port numbers) and comparing them against pre-established security rules."
    },
    {
        "id": "ecom_133",
        "subject": "E-Commerce",
        "topic": "Protecting Networks: Proxy Servers",
        "question": "What primary security benefit is provided by deploying a proxy server between an internal network and the Internet?",
        "options": [
            "It intercepts all external communications, hiding internal IP addresses from external attackers",
            "It permanently eliminates the requirement for antivirus software on corporate employee laptops",
            "It automatically refunds disputed credit card transactions without requiring bank approval",
            "It triples the physical storage capacity of internal relational database hard drive arrays"
        ],
        "answer": 0,
        "explanation": "Proxy servers act as intermediaries for all communications originating from or sent to the Internet, effectively hiding internal network IP addresses from external entities."
    },
    {
        "id": "ecom_134",
        "subject": "E-Commerce",
        "topic": "Protecting Servers & Clients",
        "question": "Why is regular anti-virus software update maintenance considered the easiest, least expensive integrity defense?",
        "options": [
            "Antivirus software relies on daily signature updates to identify newly released malicious malware code",
            "Antivirus software automatically repairs physical motherboard hardware damage caused by electrical spikes",
            "Daily antivirus updates permanently exempt web merchants from commercial sales tax liabilities",
            "Antivirus software eliminates the requirement for merchant servers to use SSL encryption certificates"
        ],
        "answer": 0,
        "explanation": "Anti-virus software is the easiest and least expensive defense against threats to system integrity, but it requires daily signature updates to protect against newly emerging viruses."
    },
    {
        "id": "ecom_135",
        "subject": "E-Commerce",
        "topic": "Security Management & Policies",
        "question": "What is the initial phase in developing an effective enterprise e-commerce security plan?",
        "options": [
            "Conducting a comprehensive risk assessment to identify assets, vulnerabilities, and threats",
            "Purchasing commercial off-the-shelf firewall hardware before establishing corporate rules",
            "Immediately terminating all remote telecommuting employee network access privileges",
            "Filing formal criminal reports with international telecommunications regulatory bodies"
        ],
        "answer": 0,
        "explanation": "Developing a security plan begins with a risk assessment—an assessment of the risks that an organization faces and the financial impact of potential security breaches."
    },
    {
        "id": "ecom_136",
        "subject": "E-Commerce",
        "topic": "Security Management & Policies",
        "question": "On average, what percentage of their total corporate IT budget do U.S. firms allocate to security hardware, software, and services?",
        "options": [
            "Approximately 12 percent of the IT budget",
            "Less than 1 percent of the IT budget",
            "More than 65 percent of the IT budget",
            "Exactly 50 percent of the IT budget"
        ],
        "answer": 0,
        "explanation": "According to industry surveys in the source material, U.S. firms and organizations spend approximately 12 percent of their total IT budget on security hardware, software, and services."
    },
    {
        "id": "ecom_137",
        "subject": "E-Commerce",
        "topic": "Traditional Payment Systems",
        "question": "Which payment method is the most common in terms of total number of transactions in the overall economy?",
        "options": [
            "Physical cash",
            "Bank checking transfers",
            "Online credit cards",
            "Merchant gift cards"
        ],
        "answer": 0,
        "explanation": "Cash is the most common form of payment in terms of the total number of transactions, offering instant convertibility into other forms of value without intermediation."
    },
    {
        "id": "ecom_138",
        "subject": "E-Commerce",
        "topic": "Traditional Payment Systems",
        "question": "What is the second most common payment method in the United States in terms of overall transaction counts?",
        "options": [
            "Checking transfers",
            "Electronic cryptocurrency",
            "Physical bartered commodities",
            "Prepaid mobile carrier minutes"
        ],
        "answer": 0,
        "explanation": "Checking transfers represent the second most common payment form in the United States in terms of total transaction volume."
    },
    {
        "id": "ecom_139",
        "subject": "E-Commerce",
        "topic": "Online Payment Systems: Credit Cards",
        "question": "What percentage of online e-commerce transactions are executed using credit cards?",
        "options": [
            "Approximately 55 percent of online payments",
            "Less than 10 percent of online payments",
            "Roughly 95 percent of online payments",
            "Exactly 28 percent of online payments"
        ],
        "answer": 0,
        "explanation": "According to the source data, credit cards account for approximately 55% of online payments, while debit cards account for about 28%."
    },
    {
        "id": "ecom_140",
        "subject": "E-Commerce",
        "topic": "Online Payment Systems: Credit Cards",
        "question": "Which of the following represents a major operational limitation of online credit card transactions for merchants?",
        "options": [
            "High merchant transaction fees (interchange) and the substantial financial risk of online fraud chargebacks",
            "Federal legal requirements that mandate all credit card transactions be settled in physical cash",
            "Inability of web servers to connect to commercial banking networks during evening weekend hours",
            "Strict limitations preventing consumers from owning more than one personal credit card account"
        ],
        "answer": 0,
        "explanation": "Key limitations of online credit cards include security risks (higher fraud and chargebacks borne by merchants), transaction fees (typically 2-4%), and social equity issues."
    },
    {
        "id": "ecom_141",
        "subject": "E-Commerce",
        "topic": "Online Credit Card Processing",
        "question": "In an online credit card transaction workflow, what is the role of the payment clearinghouse / gateway?",
        "options": [
            "Relaying authorization requests between the merchant site and the issuing bank's processing network",
            "Physically packaging customer retail items inside merchant fulfillment warehouse distribution centers",
            "Printing paper receipt copies and mailing them via registered national postal courier services",
            "Inspecting the merchant's physical server hardware components for environmental compliance"
        ],
        "answer": 0,
        "explanation": "A payment gateway/clearinghouse handles the electronic verification and routing between the merchant's shopping cart, the acquiring bank, and the customer's credit card issuing bank."
    },
    {
        "id": "ecom_142",
        "subject": "E-Commerce",
        "topic": "Alternative Payment Systems",
        "question": "How do online stored value systems like PayPal operate to facilitate peer-to-peer and merchant payments?",
        "options": [
            "By relying on funds previously deposited in an online account linked to a user's credit card or bank",
            "By minting physical gold coins and storing them in private corporate subterranean deposit vaults",
            "By requiring users to pay monthly subscription fees to municipal telecommunications utility boards",
            "By allowing consumers to settle accounts by providing personal labor to online merchants"
        ],
        "answer": 0,
        "explanation": "Online stored value systems (such as PayPal) allow consumers to make instant payments based on value stored in or linked to their bank accounts or credit cards."
    },
    {
        "id": "ecom_143",
        "subject": "E-Commerce",
        "topic": "Alternative Payment Systems",
        "question": "In a digital accumulated balance payment system, how are consumers billed for small purchases?",
        "options": [
            "Users accumulate a debit balance for micro-transactions and receive a consolidated monthly invoice",
            "Users must transmit an individual physical paper check prior to downloading each five-cent song",
            "Transactions are settled immediately by debiting the user's retirement pension fund portfolio",
            "The merchant deducts funds directly from the consumer's home municipal property tax assessment"
        ],
        "answer": 0,
        "explanation": "Digital accumulated balance systems allow users to accumulate a balance of small purchases (micropayments) over time, which is billed periodically (e.g., on a monthly statement)."
    },
    {
        "id": "ecom_144",
        "subject": "E-Commerce",
        "topic": "Alternative Payment Systems",
        "question": "What primary function does a digital wallet (e.g., Google Checkout) perform for an online shopper?",
        "options": [
            "Authenticating consumer identity, storing payment credentials, and streamlining the checkout process",
            "Physically scanning paper dollar bills inserted into a personal computer's optical disk drive",
            "Encrypting all incoming email messages received by the user's desktop operating system software",
            "Eliminating all retail sales markup added by commercial third-party wholesale distributors"
        ],
        "answer": 0,
        "explanation": "A digital wallet emulates a physical wallet by authenticating the consumer, securely storing billing and shipping information, and facilitating seamless one-click checkout across merchants."
    },
    {
        "id": "ecom_145",
        "subject": "E-Commerce",
        "topic": "Alternative Payment Systems",
        "question": "Why did early digital cash systems (token-based electronic currency) largely fail to gain widespread adoption?",
        "options": [
            "The underlying cryptographic protocols and exchange practices were too complex for mainstream users and merchants",
            "Federal regulatory authorities banned the use of computer keyboards for entering financial transaction amounts",
            "Digital tokens could only be transmitted across optical fiber cables leased directly from the United Nations",
            "Retail merchants refused to accept any payment method other than handwritten paper corporate checks"
        ],
        "answer": 0,
        "explanation": "Early digital cash experiments largely disappeared because the underlying protocols were overly complex, lacked merchant adoption, and competed against familiar credit cards."
    },
    {
        "id": "ecom_146",
        "subject": "E-Commerce",
        "topic": "Wireless Payment Systems",
        "question": "In which global regions were wireless and mobile handset payment systems first widely established?",
        "options": [
            "Japan, South Korea, and parts of Western Europe",
            "North America and rural regions of Australia",
            "Sub-Saharan Africa and isolated Pacific archipelagos",
            "Central American agricultural export zones"
        ],
        "answer": 0,
        "explanation": "Mobile handset payment systems (using contactless smart cards and mobile carrier billing) were widely established first in Europe, Japan, and South Korea."
    },
    {
        "id": "ecom_147",
        "subject": "E-Commerce",
        "topic": "Wireless Payment Systems",
        "question": "Which forms of mobile payment became prevalent early in the Japanese consumer retail marketplace?",
        "options": [
            "E-money stored value systems, mobile debit cards, and mobile credit cards",
            "Physical traveler's checks scanned through cellular phone camera sensors",
            "Bartered agricultural commodities tracked through municipal government ledgers",
            "Mandatory corporate promissory notes signed by executive employers"
        ],
        "answer": 0,
        "explanation": "Japanese mobile payment systems successfully integrated e-money (contactless stored value), mobile debit, and mobile credit cards into everyday mobile handsets."
    },
    {
        "id": "ecom_148",
        "subject": "E-Commerce",
        "topic": "Underground Economy",
        "question": "What is the primary role of 'underground economy marketplaces' in modern cybercrime syndicates?",
        "options": [
            "Trading stolen credit card data, harvested personal credentials, and compromised botnet access",
            "Hosting legitimate public domain software archives to assist academic university researchers",
            "Providing discounted hardware components to commercial third-party web hosting data centers",
            "Publishing government regulatory compliance filings for publicly traded financial enterprises"
        ],
        "answer": 0,
        "explanation": "Underground economy marketplaces operate on hidden servers to traffic stolen credit card information, bank credentials, identity profiles, and malware toolkits."
    },
    {
        "id": "ecom_149",
        "subject": "E-Commerce",
        "topic": "Security Policy & Audit",
        "question": "What is the primary objective of conducting a routine cybersecurity audit on an e-commerce platform?",
        "options": [
            "Reviewing security logs and evaluating whether existing technical controls conform to security policy",
            "Calculating the total corporate payroll taxes owed to federal revenue collection agencies",
            "Replacing all server hard drive arrays with optical magnetic storage tape cartridges",
            "Measuring customer satisfaction ratings concerning graphic design typography on the homepage"
        ],
        "answer": 0,
        "explanation": "A security audit involves reviewing system logs, testing technical controls, and verifying whether operational practices comply with established organizational security policies."
    },
    {
        "id": "ecom_150",
        "subject": "E-Commerce",
        "topic": "Security Management & Policies",
        "question": "Why is security said to 'break at the weakest link' in an enterprise e-commerce environment?",
        "options": [
            "An attacker only needs to exploit one overlooked vulnerability to compromise an otherwise secure system",
            "Hardware routers will automatically shut down if a single employee forgets their login password",
            "Symmetric encryption algorithms lose all cryptographic strength if applied to long text files",
            "Digital certificate authorities revoke web server licenses whenever network traffic increases"
        ],
        "answer": 0,
        "explanation": "Security often breaks at the weakest link because sophisticated technical perimeter defenses are rendered useless if an attacker exploits a single human lapse, software bug, or misconfiguration."
    }
]
