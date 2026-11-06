# scripts/refine_all_batches.py
"""
This script loads the 4 batches, applies targeted distractor refinements so that
distractors are equal or longer than the correct answer in ~85-90% of questions,
shuffles/balances the answer positions so exactly 50 are index 0, 50 are index 1,
50 are index 2, and 50 are index 3, and returns the refined 200 questions.
"""

import sys
sys.path.append('scripts')
from build_batch1 import questions_batch1
from build_batch2 import questions_batch2
from build_batch3 import questions_batch3
from build_batch4 import questions_batch4
import random

all_qs = questions_batch1 + questions_batch2 + questions_batch3 + questions_batch4

# Dictionary of targeted distractor improvements by question id
# {qid: {old_opt: new_opt}}
refinements = {
    # Batch 1
    "ecom_2": {
        "Restricting electronic service interactions to regional buyers":
        "Restricting electronic service interactions exclusively to regional buyers"
    },
    "ecom_3": {
        "As an automated accounting mechanism for physical store locations":
        "As an automated accounting mechanism for physical brick-and-mortar retail locations"
    },
    "ecom_6": {
        "Pure traditional commerce":
        "Pure traditional physical commerce"
    },
    "ecom_7": {
        "A government agency monitoring corporate accounting compliance records":
        "A government agency actively monitoring corporate accounting compliance records"
    },
    "ecom_9": {
        "B2B eliminates the requirement for secure telecommunications links":
        "B2B completely eliminates the operational requirement for secure telecommunications links"
    },
    "ecom_10": {
        "Suppliers are completely insulated from changing customer buying demands":
        "Suppliers are completely insulated from changing and dynamic customer buying demands"
    },
    "ecom_17": {
        "By requiring foreign consumers to sign exclusive physical supply covenants":
        "By requiring foreign consumers to sign exclusive physical supply covenants in advance"
    },
    "ecom_18": {
        "Legal depreciation costs of manufacturing robotics and assembly lines":
        "Legal depreciation costs of heavy manufacturing robotics and physical assembly lines"
    },
    "ecom_21": {
        "The Internet eliminates all digital network encryption overhead protocols":
        "The Internet completely eliminates all digital network encryption overhead protocols online"
    },
    "ecom_23": {
        "By preventing consumers from comparing product specifications across brands":
        "By preventing prospective consumers from comparing product specifications across brands"
    },
    "ecom_25": {
        "Restriction of purchases to locally manufactured domestic merchandise":
        "Mandatory restriction of purchases to locally manufactured domestic merchandise"
    },
    "ecom_26": {
        "Heavy industrial components requiring freight delivery":
        "Heavy industrial manufacturing components requiring specialized freight delivery"
    },
    "ecom_27": {
        "They transfer ownership of platform infrastructure to visiting consumers":
        "They permanently transfer ownership of platform infrastructure to visiting consumers"
    },
    "ecom_28": {
        "Guaranteeing that every auctioned item includes a lifetime warranty":
        "Legally guaranteeing that every auctioned item includes a full lifetime warranty"
    },
    "ecom_31": {
        "By restricting low-cost merchandise distribution exclusively to big cities":
        "By restricting low-cost merchandise distribution exclusively to dense metropolitan cities"
    },
    "ecom_32": {
        "By automatically converting national currencies into physical precious metals":
        "By automatically converting all national currencies into physical precious metals"
    },
    "ecom_34": {
        "Mobile devices are legally restricted from displaying commercial advertisements":
        "Mobile handheld devices are legally restricted from displaying commercial advertisements"
    },
    "ecom_39": {
        "Incompatibility between regional optical fiber cables and copper phone wiring":
        "Physical incompatibility between regional optical fiber cables and copper phone wiring"
    },
    "ecom_44": {
        "Support services":
        "External support services"
    },
    "ecom_45": {
        "By centralizing all corporate operational authority strictly within headquarters":
        "By centralizing all corporate operational authority strictly within global headquarters"
    },
    "ecom_46": {
        "By generating printed monthly customer surveys for standard postal delivery":
        "By generating printed monthly customer feedback surveys for standard physical postal delivery"
    },
    "ecom_47": {
        "They eliminate the need for corporate procurement departments and supply chains":
        "They completely eliminate the need for corporate procurement departments and supply chains"
    },
    "ecom_48": {
        "It requires physical currency to be scanned through specialized desktop optical readers":
        "It strictly requires physical currency to be scanned through specialized desktop optical readers"
    },
    "ecom_49": {
        "B2C web storefronts require significantly more telecommunications bandwidth than B2B":
        "B2C consumer web storefronts require significantly more telecommunications bandwidth than B2B"
    },

    # Batch 2
    "ecom_54": {
        "Restricting product return periods to within two hours of initial web placement":
        "Strictly restricting product return periods to within two hours of initial web placement"
    },
    "ecom_57": {
        "The subscription revenue model":
        "The recurring subscription revenue model"
    },
    "ecom_59": {
        "The legal jurisdiction governing corporate intellectual property disputes":
        "The specific legal jurisdiction governing corporate intellectual property disputes"
    },
    "ecom_60": {
        "Telecommunications carriers restrict websites to displaying fifty products at once":
        "Telecommunications carriers strictly restrict commercial websites to displaying fifty products"
    },
    "ecom_61": {
        "Direct competitors are legally obligated to share their confidential customer databases":
        "Direct competitors are legally obligated to openly share their confidential customer databases"
    },
    "ecom_62": {
        "Total number of printed pages contained in corporate human resources handbooks":
        "The total number of printed administrative pages contained in corporate human resources handbooks"
    },
    "ecom_63": {
        "When it relies exclusively on third-party marketing agencies for customer acquisition":
        "When it relies almost exclusively on external third-party marketing agencies for customer acquisition"
    },
    "ecom_64": {
        "When buyer and seller computers operate on completely different processor architectures":
        "When transacting buyer and seller computers operate on completely different processor architectures"
    },
    "ecom_65": {
        "First movers cannot collect credit card payments until subsequent competitors enter":
        "First-mover firms cannot process credit card payments until subsequent competitors enter the market"
    },
    "ecom_67": {
        "Commercial off-the-shelf operating system licenses acquired through retail channels":
        "Standard commercial off-the-shelf operating system licenses acquired through conventional retail channels"
    },
    "ecom_68": {
        "Documenting internal payroll deductions for corporate employee pension plans":
        "Formally documenting all internal payroll deductions for corporate employee retirement pension plans"
    },
    "ecom_69": {
        "Functional management departments are completely eliminated in favor of manual labor":
        "Internal functional management departments are completely eliminated in favor of manual physical labor"
    },
    "ecom_70": {
        "Management teams with corporate backgrounds guarantee immunity from competitor lawsuits":
        "Management teams possessing corporate backgrounds guarantee absolute immunity from competitor lawsuits"
    },
    "ecom_74": {
        "Independent digital exchange brokering":
        "Independent digital marketplace exchange brokering"
    },
    "ecom_76": {
        "Requiring consumers to surrender physical stock certificates before reading":
        "Mandatorily requiring consumers to surrender physical stock certificates before reading web pages"
    },
    "ecom_77": {
        "Content owners are legally prohibited from collecting subscription fees from retail web consumers":
        "Commercial content owners are strictly prohibited by law from collecting subscription fees from retail consumers"
    },
    "ecom_79": {
        "Providing free residential broadband telecommunications connections to homes":
        "Providing completely free residential broadband telecommunications connections directly to consumer homes"
    },
    "ecom_80": {
        "They purchase wholesale inventory and warehouse physical items before retail resale":
        "They routinely purchase wholesale inventory and warehouse physical merchandise items before retail resale"
    },
    "ecom_82": {
        "Restricting member access to individuals holding corporate executive management positions":
        "Strictly restricting platform member access to individuals holding corporate executive management positions"
    },
    "ecom_83": {
        "It acts as a consumer auction intermediary matching individual collectors of rare antique items":
        "It operates as an open consumer auction intermediary matching individual collectors of rare antique items"
    },
    "ecom_86": {
        "Independent exchanges were legally required to charge 90 percent transaction commissions":
        "Independent exchanges were legally obligated by financial regulators to charge 90 percent transaction commissions"
    },
    "ecom_87": {
        "Industry consortia serve broad horizontal markets across all consumer packaged retail merchandise":
        "Industry consortia primarily serve broad horizontal retail markets across all consumer packaged retail merchandise"
    },
    "ecom_92": {
        "They are legally exempt from paying corporate taxes under nineteenth-century mining acts":
        "They are legally exempt from paying domestic corporate taxes under historic nineteenth-century mining statutes"
    },
    "ecom_93": {
        "It prevents buyers from comparing warranty terms across competing manufacturer websites":
        "It strictly prevents prospective buyers from comparing warranty terms across competing manufacturer websites"
    },
    "ecom_94": {
        "It drastically increases entry barriers by requiring massive physical store construction":
        "It drastically increases commercial entry barriers by requiring massive physical retail store network construction"
    },
    "ecom_98": {
        "By legally shielding the corporation from having to pay overtime wages to physical laborers":
        "By legally shielding the commercial corporation from having to pay standard overtime wages to physical laborers"
    },

    # Batch 3
    "ecom_101": {
        "System availability":
        "Guaranteed system availability"
    },
    "ecom_103": {
        "Ensuring that delivered physical parcels are delivered within twenty-four hours of ordering":
        "Ensuring that all delivered physical parcels are successfully delivered within twenty-four hours of ordering"
    },
    "ecom_104": {
        "Confidentiality is managed by public laws; privacy is enforced exclusively through network routers":
        "Confidentiality is managed by international public laws; privacy is enforced exclusively through network routers"
    },
    "ecom_106": {
        "Adding security mechanisms automatically doubles consumer broadband connection transmission speeds":
        "Adding complex security mechanisms automatically doubles consumer broadband telecommunications transmission speeds"
    },
    "ecom_107": {
        "The marketing advertising agency, the print media catalog, and the retail storefront":
        "The commercial marketing advertising agency, the print media catalog, and the physical retail storefront"
    },
    "ecom_108": {
        "A virus spreads exclusively through physical optical laser cables between data centers":
        "A virus spreads exclusively through physical undersea optical laser cables connecting regional data centers"
    },
    "ecom_110": {
        "An authorized consortium of banking servers managing international currency settlements":
        "An authorized interbank consortium of mainframe servers managing international sovereign currency settlements"
    },
    "ecom_113": {
        "Pharming requires physical access to a user's office keyboard and monitor hardware":
        "Pharming technically requires direct physical access to a user's corporate office keyboard and monitor hardware"
    },
    "ecom_115": {
        "White hats operate exclusively on government networks while black hats target private merchants":
        "White hats operate almost exclusively on federal government networks while black hats target private retail merchants"
    },
    "ecom_116": {
        "By physically cutting the undersea fiber-optic cables servicing the merchant's hosting facility":
        "By physically severing the undersea fiber-optic telecommunications cables servicing the merchant's hosting facility"
    },
    "ecom_117": {
        "Compressing video streams to improve mobile device streaming performance across 3G networks":
        "Compressing high-definition video streams to improve mobile device streaming performance across 3G cellular networks"
    },
    "ecom_118": {
        "Accidental electrical failures occurring at third-party web hosting data centers":
        "Accidental catastrophic electrical power failures occurring at third-party commercial web hosting data centers"
    },
    "ecom_120": {
        "The sender uses a public key while the receiver uses a completely unrelated private password":
        "The sender encrypts using an open public key while the receiver uses a completely unrelated private login password"
    },
    "ecom_122": {
        "The cipher cannot be processed by computers using standard commercial microprocessors":
        "The cipher algorithm cannot be processed by computer systems using standard commercial off-the-shelf microprocessors"
    },
    "ecom_123": {
        "By requiring both transacting parties to meet physically to exchange printed keycards":
        "By requiring both transacting commercial parties to meet physically in person to exchange printed cryptographic keycards"
    },
    "ecom_125": {
        "Compressing high-definition video files so they stream smoothly over low-bandwidth connections":
        "Compressing high-definition streaming video files so they broadcast smoothly over low-bandwidth cellular connections"
    },
    "ecom_126": {
        "By typing the sender's legal full name at the bottom of an unencrypted text message":
        "By typing the message sender's official legal full name at the bottom of an unencrypted plaintext email message"
    },
    "ecom_127": {
        "It uses public key cryptography to encrypt massive video files and symmetric keys for short email headers":
        "It uses public key cryptography to encrypt massive multimedia files and symmetric keys for short email headers"
    },
    "ecom_128": {
        "Processing credit card chargebacks when online consumers dispute merchandise purchases":
        "Routinely processing credit card chargebacks and refunds when online consumers dispute physical merchandise purchases"
    },
    "ecom_129": {
        "The client computer disables local operating system security patches to increase processing speed":
        "The client computer systematically disables local operating system security patches to increase raw processing speed"
    },
    "ecom_130": {
        "S-HTTP operates exclusively across private corporate intranets and cannot access the Internet":
        "S-HTTP operates exclusively across private internal corporate intranets and cannot transmit data across the open Internet"
    },
    "ecom_132": {
        "By analyzing the emotional sentiment expressed within the text content of user email messages":
        "By analyzing the subjective emotional sentiment expressed within the text content of individual user email messages"
    },
    "ecom_133": {
        "It automatically refunds disputed credit card transactions without requiring bank approval":
        "It automatically authorizes full refunds for disputed credit card transactions without requiring merchant bank approval"
    },
    "ecom_134": {
        "Antivirus software automatically repairs physical motherboard hardware damage caused by electrical spikes":
        "Antivirus software automatically repairs severe physical motherboard hardware damage caused by lightning electrical spikes"
    },
    "ecom_135": {
        "Purchasing commercial off-the-shelf firewall hardware before establishing corporate rules":
        "Purchasing commercial off-the-shelf enterprise firewall hardware appliances before establishing corporate policy rules"
    },
    "ecom_140": {
        "Federal legal requirements that mandate all credit card transactions be settled in physical cash":
        "Federal statutory legal requirements that mandate all commercial credit card transactions be settled in physical paper cash"
    },
    "ecom_141": {
        "Printing paper receipt copies and mailing them via registered national postal courier services":
        "Printing duplicate physical paper receipt copies and mailing them via registered national government postal courier services"
    },
    "ecom_142": {
        "By requiring users to pay monthly subscription fees to municipal telecommunications utility boards":
        "By requiring registered users to pay recurring monthly subscription fees to municipal telecommunications utility boards"
    },
    "ecom_143": {
        "Users must transmit an individual physical paper check prior to downloading each five-cent song":
        "Users must physically mail an individual paper bank check to the merchant prior to downloading each five-cent audio track"
    },
    "ecom_144": {
        "Physically scanning paper dollar bills inserted into a personal computer's optical disk drive":
        "Physically scanning paper currency dollar bills inserted into a personal desktop computer's optical laser disk drive tray"
    },
    "ecom_145": {
        "Federal regulatory authorities banned the use of computer keyboards for entering financial transaction amounts":
        "Federal regulatory banking authorities strictly banned the use of computer keyboards for entering financial transaction amounts"
    },
    "ecom_147": {
        "Physical traveler's checks scanned through cellular phone camera sensors":
        "Physical paper traveler's checks scanned directly through mobile cellular phone camera sensors"
    },
    "ecom_148": {
        "Hosting legitimate public domain software archives to assist academic university researchers":
        "Hosting fully legitimate public domain open-source software archives to assist academic university scientific researchers"
    },
    "ecom_149": {
        "Replacing all server hard drive arrays with optical magnetic storage tape cartridges":
        "Physically replacing all internal server hard drive storage arrays with optical magnetic backup tape cartridges"
    },
    "ecom_150": {
        "Hardware routers will automatically shut down if a single employee forgets their login password":
        "Enterprise hardware routers will automatically shut down if a single corporate employee forgets their network login password"
    },

    # Batch 4
    "ecom_151": {
        "Negotiating international maritime shipping contracts and purchasing retail warehouses":
        "Negotiating complex international maritime shipping contracts and purchasing regional physical retail warehouses"
    },
    "ecom_153": {
        "Guaranteeing that all hardware components will operate indefinitely without maintenance":
        "Guaranteeing that all enterprise hardware server components will operate indefinitely without routine technical maintenance"
    },
    "ecom_154": {
        "Hardware procurement, marketing advertising, code deployment, auditing, and bankruptcy":
        "Hardware procurement, marketing advertising campaigns, code deployment, financial auditing, and corporate bankruptcy"
    },
    "ecom_155": {
        "The legal articles of incorporation filed with state commercial licensing agencies":
        "The official legal articles of incorporation formally filed with state commercial business licensing agencies"
    },
    "ecom_156": {
        "They specify the marketing advertising slogans broadcast during televised sports events":
        "They specify the national marketing advertising campaign slogans broadcast during televised professional sports events"
    },
    "ecom_157": {
        "The total number of printed paper manuals delivered to customer support agents":
        "The total aggregate number of printed paper operational manuals delivered to telephone customer support agents"
    },
    "ecom_159": {
        "A sworn legal affidavit verifying full compliance with federal securities regulations":
        "A sworn legal judicial affidavit formally verifying full compliance with federal commercial securities regulations"
    },
    "ecom_160": {
        "Commercial broadband telecommunications vendor service contracts":
        "Formal multi-year commercial broadband telecommunications vendor service-level contracts"
    },
    "ecom_161": {
        "The psychological motivations influencing consumer purchasing choices online":
        "The complex psychological motivations and cognitive biases influencing consumer purchasing choices online"
    },
    "ecom_162": {
        "The site will be legally barred from connecting to the public Internet telecommunications grid":
        "The completed site will be legally barred from connecting to the public Internet commercial telecommunications grid"
    },
    "ecom_163": {
        "The hosting provider assumes complete ownership and legal responsibility for merchant inventory":
        "The third-party hosting provider assumes complete legal ownership and physical responsibility for all merchant inventory"
    },
    "ecom_165": {
        "System testing checks only whether graphic images contain valid copyright metadata headers":
        "System testing evaluates only whether catalog graphic images contain valid digital copyright metadata headers"
    },
    "ecom_166": {
        "Measuring the physical electrical consumption of server computer power supply transformers":
        "Measuring the real-time physical electrical power consumption of server computer power supply transformers"
    },
    "ecom_167": {
        "Hardware microprocessors must be physically replaced with new models every thirty days":
        "Hardware microprocessors and motherboards must be physically removed and replaced with new models every thirty days"
    },
    "ecom_168": {
        "Physically marking server equipment cabinets with serial barcodes for warehouse asset tracking":
        "Physically scanning and marking server equipment cabinets with serial barcodes for warehouse hardware asset tracking"
    },
    "ecom_169": {
        "Undersea fiber-optic cable ownership shares purchased from international maritime authorities":
        "Direct undersea fiber-optic cable ownership equity shares purchased from international maritime transit authorities"
    },
    "ecom_171": {
        "To restrict website visitor access exclusively to users connecting through corporate local area networks":
        "To strictly restrict website visitor access exclusively to users connecting through internal corporate local area networks"
    },
    "ecom_173": {
        "NCSA Common Gateway Interface":
        "National Center for Supercomputing Applications Common Gateway Interface"
    },
    "ecom_174": {
        "Processing international currency exchange rates on credit purchases":
        "Processing dynamic international currency exchange rates on foreign credit card purchases"
    },
    "ecom_177": {
        "It eliminates the requirement for secure credit card verification clearinghouses during checkout":
        "It permanently eliminates the requirement for secure credit card verification clearinghouses during online checkout"
    },
    "ecom_178": {
        "Serving static HTML image files directly to web browsers without accessing internal data stores":
        "Serving static HTML image files directly to client web browsers without ever accessing internal database storage layers"
    },
    "ecom_180": {
        "Physical chassis weight of the plastic packaging containing software installation optical discs":
        "The physical chassis weight of the plastic retail packaging containing software installation optical compact discs"
    },
    "ecom_181": {
        "It transfers complete corporate stock equity ownership directly to third-party telecommunications vendors":
        "It permanently transfers complete corporate stock equity ownership directly to third-party telecommunications vendors"
    },
    "ecom_182": {
        "Operating web server software on consumer desktop workstations to eliminate server equipment expenses":
        "Operating production web server software on consumer desktop workstations to eliminate dedicated server equipment expenses"
    },
    "ecom_185": {
        "SSL encryption completely eliminates the requirement for random access memory in server motherboards":
        "SSL encryption protocols completely eliminate the operational requirement for random access memory in server motherboards"
    },
    "ecom_186": {
        "By physically mounting server equipment cabinets vertically along the walls of the corporate cafeteria":
        "By physically mounting server equipment hardware cabinets vertically along the walls of the corporate cafeteria hallway"
    },
    "ecom_189": {
        "Purchasing all physical telecommunications optical fiber cables connecting competitor retail data centers":
        "Purchasing all physical telecommunications optical fiber cabling routes connecting competitor retail data centers"
    },
    "ecom_191": {
        "A hardware failure occurring when two computer server processors overheat inside a data center cabinet":
        "A catastrophic hardware failure occurring when two computer server processors overheat inside a data center cabinet"
    },
    "ecom_194": {
        "Restricting database connectivity exclusively to flat text files formatted in comma-separated values":
        "Strictly restricting database connectivity exclusively to flat text files formatted in comma-separated value lines"
    },
    "ecom_195": {
        "It forces web browsers to reload the entire web page and re-render all images for every mouse click":
        "It continually forces web browsers to reload the entire web page and re-render all graphics for every visitor mouse click"
    },
    "ecom_197": {
        "By automatically transmitting confidential consumer bank account passwords to online merchants":
        "By automatically transmitting confidential consumer banking account login passwords to visiting online retail merchants"
    },
    "ecom_199": {
        "Mandating that commercial web hosting facilities be constructed within five miles of municipal airports":
        "Mandating that commercial web hosting data center facilities be constructed within five miles of municipal civil airports"
    },
    "ecom_200": {
        "Federal commercial laws assess severe tax penalties on corporations that deploy enterprise application servers":
        "Federal commercial trade laws assess severe financial tax penalties on corporations that deploy enterprise application servers"
    }
}

# Apply refinements
for q in all_qs:
    qid = q["id"]
    if qid in refinements:
        for old_txt, new_txt in refinements[qid].items():
            if old_txt in q["options"]:
                idx = q["options"].index(old_txt)
                q["options"][idx] = new_txt

# Now balance answer positions: exactly 50 of 0, 50 of 1, 50 of 2, 50 of 3
# Create target distribution
target_positions = [0]*50 + [1]*50 + [2]*50 + [3]*50
# Shuffle with fixed seed for deterministic, uniform spread
rng = random.Random(1337)
rng.shuffle(target_positions)

for i, q in enumerate(all_qs):
    cur_ans_text = q["options"][q["answer"]]
    tgt = target_positions[i]
    if q["answer"] != tgt:
        opts = list(q["options"])
        opts.remove(cur_ans_text)
        opts.insert(tgt, cur_ans_text)
        q["options"] = opts
        q["answer"] = tgt

# Verify stats
from collections import Counter
pos = Counter(q["answer"] for q in all_qs)
print("Answer positions:", sorted(pos.items()))

longest = 0
for i, q in enumerate(all_qs):
    lens = [len(o) for o in q["options"]]
    a = q["answer"]
    if lens[a] == max(lens) and lens.count(max(lens)) == 1:
        longest += 1
print(f"Correct strictly longest: {longest} / 200 ({100*longest/200:.1f}%)")

# Save refined questions to questions/ecom_questions.json
import json
with open("questions/ecom_questions.json", "w", encoding="utf-8") as f:
    json.dump(all_qs, f, indent=2, ensure_ascii=False)
print("Successfully wrote questions/ecom_questions.json!")
