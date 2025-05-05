from utils import write_selected_dict_values_to_file

CloudProjects = [
    {
        "ID": 1,
        "title": "Secure Remote Communication Using DES Algorithm",
        "description": "A system for secure data transfer over unsecure networks using the Data Encryption Standard (DES) algorithm, widely used by companies, governments, and military.",
        "category": ["Cloud Computing", "Security and Encryption", "Web | Desktop Application"],
        "required_skills": ["DES Algorithm", "Network Security", "Data Encryption"],
        "proposed_algorithms": ["DES"]
    },
    {
        "ID": 2,
        "title": "Secure File Storage On Cloud Using Hybrid Cryptography",
        "description": "A system that ensures secure file storage on the cloud using a hybrid cryptography approach involving Blowfish and splitting/merging techniques.",
        "category": ["Cloud Computing", "Security and Encryption", "Web | Desktop Application"],
        "required_skills": ["Blowfish Encryption", "Hybrid Cryptography", "Cloud Security"],
        "proposed_algorithms": ["Blowfish", "Hybrid Cryptography"]
    },
    {
        "ID": 3,
        "title": "Secure Data Transfer Over Internet Using Image Steganography",
        "description": "A system using image steganography to hide sensitive information within images for secure data transfer over the internet.",
        "category": ["Cloud Computing", "Networking", "Parallel And Distributed System", "Security and Encryption", "Web | Desktop Application"],
        "required_skills": ["Image Steganography", "Data Hiding", "Cryptography"],
        "proposed_algorithms": ["Steganography"]
    },
    {
        "ID": 4,
        "title": "Secure Backup Software System",
        "description": "A Windows application for secure storage of files, documents, images, and videos, with access restricted to authorized users only.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Backup Software", "File Encryption", "SQL Database"],
        "proposed_algorithms": ["File Encryption"]
    },
    {
        "ID": 5,
        "title": "Policy-by-Example for Online Social Networks",
        "description": "A system to improve privacy policy management in online social networks using clustering techniques and memory-based policy setting.",
        "category": ["Cloud Computing", "Data Mining", "Security and Encryption"],
        "required_skills": ["Privacy Policy Management", "Clustering Techniques", "Social Networks"],
        "proposed_algorithms": ["Clustering"]
    },
    {
        "ID": 6,
        "title": "Web Usage Mining Using Improved Frequent Pattern Tree Algorithms",
        "description": "A system for discovering and analyzing user access patterns on websites using improved frequent pattern tree algorithms.",
        "category": ["Cloud Computing", "Data Mining"],
        "required_skills": ["Web Usage Mining", "Frequent Pattern Tree", "Log File Analysis"],
        "proposed_algorithms": ["Frequent Pattern Tree"]
    },
    {
        "ID": 7,
        "title": "Reversible Data Hiding With Optimal Value Transfer",
        "description": "A system for reversible data hiding where original host content can be perfectly restored after data extraction, using optimal value transfer rules.",
        "category": ["Cloud Computing", "Data Mining"],
        "required_skills": ["Data Hiding", "Optimal Value Transfer", "Image Processing"],
        "proposed_algorithms": ["Reversible Data Hiding"]
    },
    {
        "ID": 8,
        "title": "Public Auditing Cloud Data Storage - Bilinear Pairing",
        "description": "A mechanism to ensure reliable data storage using cloud services, employing bilinear pairing for public auditing of data.",
        "category": ["Cloud Computing", "Data Mining"],
        "required_skills": ["Cloud Security", "Bilinear Pairing", "Public Auditing"],
        "proposed_algorithms": ["Bilinear Pairing"]
    },
    {
        "ID": 9,
        "title": "Optimization of Horizontal Aggregation in SQL by Using K-Means Clustering",
        "description": "A system to optimize horizontal aggregation in SQL using K-Means clustering, improving data analysis efficiency.",
        "category": ["Cloud Computing", "Data Mining"],
        "required_skills": ["SQL", "K-Means Clustering", "Data Aggregation"],
        "proposed_algorithms": ["K-Means Clustering"]
    },
    {
        "ID": 10,
        "title": "Access Control Mechanisms for Outsourced Data in Cloud",
        "description": "A two-level access control scheme for securing outsourced data in the cloud, protecting both data confidentiality and user access patterns.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Access Control", "Cloud Security", "Data Confidentiality"],
        "proposed_algorithms": ["Access Control Mechanism"]
    },
    {
        "ID": 11,
        "title": "Building Confidential and Efficient Query Services in the Cloud with RASP Data Perturbation",
        "description": "A secure and efficient query service in the cloud using RASP data perturbation, combining order-preserving encryption and dimensionality expansion.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Query Services", "RASP Data Perturbation", "Cloud Security"],
        "proposed_algorithms": ["RASP Data Perturbation"]
    },
    {
        "ID": 12,
        "title": "Balancing Performance, Accuracy, and Precision for Secure Cloud Transactions",
        "description": "A framework to ensure trusted transactions on cloud servers by enforcing policy consistency constraints and using a Two-Phase Validation Commit protocol.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Cloud Transactions", "Policy Consistency", "Two-Phase Validation Commit"],
        "proposed_algorithms": ["Two-Phase Validation Commit"]
    },
    {
        "ID": 13,
        "title": "Secure Data Retrieval for Decentralized Disruption-Tolerant Military Networks",
        "description": "A system for secure data retrieval in decentralized disruption-tolerant military networks using Ciphertext-policy attribute-based encryption (CP-ABE).",
        "category": ["Cloud Computing", "Networking", "Security and Encryption", "Web | Desktop Application"],
        "required_skills": ["CP-ABE", "Network Security", "Disruption-Tolerant Networks"],
        "proposed_algorithms": ["CP-ABE"]
    },
    {
        "ID": 14,
        "title": "Product Aspect Ranking and Its Applications",
        "description": "A framework for identifying important product aspects from online consumer reviews to improve usability and information navigation.",
        "category": ["Cloud Computing", "Data Mining", "Security and Encryption", "Web | Desktop Application"],
        "required_skills": ["Product Aspect Ranking", "Consumer Review Analysis", "Data Mining"],
        "proposed_algorithms": ["Aspect Ranking"]
    },
    {
        "ID": 15,
        "title": "Typicality-Based Collaborative Filtering Recommendation",
        "description": "A novel collaborative filtering recommendation method using object typicality from cognitive psychology to improve recommendation accuracy.",
        "category": ["Cloud Computing", "Data Mining", "Security and Encryption"],
        "required_skills": ["Collaborative Filtering", "Recommendation Systems", "Cognitive Psychology"],
        "proposed_algorithms": ["TyCo"]
    },
    {
        "ID": 16,
        "title": "Panda: Public Auditing for Shared Data with Efficient User Revocation in the Cloud",
        "description": "A system for ensuring shared data integrity in the cloud through public auditing and efficient user revocation.",
        "category": ["Cloud Computing", "Data Mining", "Parallel And Distributed System", "Security and Encryption", "Web | Desktop Application"],
        "required_skills": ["Public Auditing", "Cloud Security", "User Revocation"],
        "proposed_algorithms": ["Public Auditing"]
    },
    {
        "ID": 17,
        "title": "Identity-Based Distributed Provable Data Possession in Multicloud Storage",
        "description": "A protocol for remote data integrity checking in multi-cloud storage, ensuring data integrity without downloading the entire data.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Data Integrity", "Multi-Cloud Storage", "Provable Data Possession"],
        "proposed_algorithms": ["ID-DPDP"]
    },
    {
        "ID": 18,
        "title": "Control Cloud Data Access Privilege and Anonymity with Fully Anonymous Attribute-Based Encryption",
        "description": "A semi-anonymous privilege control scheme for securing cloud storage, decentralizing authority to limit identity leakage.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Attribute-Based Encryption", "Cloud Security", "Access Control"],
        "proposed_algorithms": ["AnonyControl"]
    },
    {
        "ID": 19,
        "title": "A Secure and Dynamic Multi-keyword Ranked Search Scheme over Encrypted Cloud Data",
        "description": "A multi-keyword ranked search scheme over encrypted cloud data, preserving privacy and enabling efficient retrieval.",
        "category": ["Cloud Computing", "Security and Encryption"],
        "required_skills": ["Multi-keyword Search", "Cloud Data Encryption", "Data Retrieval"],
        "proposed_algorithms": ["MRSE"]
    },
    {
        "ID": 20,
        "title": "CloudProtect: Managing Data Privacy in Cloud Applications",
        "description": "The CloudProtect middleware allows users to encrypt sensitive data within various cloud applications while preserving all functionalities.",
        "category":

 ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Data Privacy", "Encryption", "Cloud Applications"],
        "proposed_algorithms": ["CloudProtect"]
    },
    {
        "ID": 21,
        "title": "A Secured Cost-effective Multi-Cloud Storage in Cloud Computing",
        "description": "A multi-cloud storage system that divides user data blocks into pieces, ensuring data availability and privacy.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Multi-Cloud Storage", "Data Privacy", "Cost-effective Solutions"],
        "proposed_algorithms": ["Data Splitting"]
    },
    {
        "ID": 22,
        "title": "Ensuring Data Storage Security in Cloud Computing",
        "description": "A distributed scheme for ensuring the correctness of users' data in the cloud using homomorphic token with distributed verification.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Data Storage Security", "Homomorphic Token", "Distributed Verification"],
        "proposed_algorithms": ["Homomorphic Token"]
    },
    {
        "ID": 23,
        "title": "Fuzzy Keyword Search over Encrypted Data in Cloud Computing",
        "description": "A system for effective fuzzy keyword search over encrypted cloud data, enhancing usability by returning closely matching files.",
        "category": ["Cloud Computing"],
        "required_skills": ["Fuzzy Keyword Search", "Data Encryption", "Usability"],
        "proposed_algorithms": ["Fuzzy Keyword Search"]
    },
    {
        "ID": 24,
        "title": "Developing Secure Social Healthcare System over the Cloud",
        "description": "A social media application for healthcare developed over the cloud, ensuring security through role-based access control.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Healthcare Applications", "Cloud Security", "Role-Based Access Control"],
        "proposed_algorithms": ["Role-Based Access Control"]
    },
    {
        "ID": 25,
        "title": "Access Control Mechanisms for Outsourced Data in Cloud",
        "description": "A two-level access control scheme for securing outsourced data in the cloud, protecting both data confidentiality and user access patterns.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Access Control", "Cloud Security", "Data Confidentiality"],
        "proposed_algorithms": ["Access Control Mechanism"]
    },
    {
        "ID": 26,
        "title": "Cloud Data Protection for the Masses",
        "description": "A cloud platform architecture called Data Protection as a Service, offering strong data protection while enabling rich applications.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Data Protection", "Cloud Security", "Application Development"],
        "proposed_algorithms": ["Data Protection as a Service"]
    },
    {
        "ID": 27,
        "title": "Dynamic Bandwidth Allocation in Cloud Computing",
        "description": "A method for reallocating bandwidth dynamically from passive users to active users in cloud computing environments.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Bandwidth Allocation", "Cloud Networking", "Dynamic Resource Management"],
        "proposed_algorithms": ["Bandwidth Allocation"]
    },
    {
        "ID": 28,
        "title": "Defenses Against Large Scale Online Password Guessing Attacks by Using Persuasive Click Points",
        "description": "A graphical password system using persuasive click points to defend against large-scale online password guessing attacks.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Graphical Passwords", "Security", "Usable Security"],
        "proposed_algorithms": ["Persuasive Click Points"]
    },
    {
        "ID": 29,
        "title": "Efficient Privacy-Preserving Range Queries over Encrypted Data in Cloud Computing",
        "description": "A method for efficient privacy-preserving range queries over encrypted data in cloud computing using secure comparison protocols.",
        "category": ["Cloud Computing", "Web | Desktop Application"],
        "required_skills": ["Range Queries", "Data Encryption", "Privacy Preservation"],
        "proposed_algorithms": ["Secure Comparison Protocol"]
    }
]


# adding indices
for i,proj in enumerate(CloudProjects):
    proj['ID'] = i+1

links = [
"https://projectideas.co.in/secure-remote-communication-using-des-algorithm-dotnet/",
"https://projectideas.co.in/secure-file-storage-on-cloud-using-hybrid-cryptography-dotnet/",
"https://projectideas.co.in/secure-data-transfer-over-internet-using-image-steganography/",
"https://projectideas.co.in/secure-backup-software-system-project-ideas/",
"https://projectideas.co.in/policy-example-online-social-networks/",
"https://projectideas.co.in/web-usage-mining-using-improved-frequent-pattern-tree-algorithms/",
"https://projectideas.co.in/reversible-data-hiding-optimal-value-transfer/",
"https://projectideas.co.in/public-auditing-cloud-data-storage-bilinear-pairing/",
"https://projectideas.co.in/optimization-horizontal-aggregation-sql-using-k-means-clustering/",
"https://projectideas.co.in/access-control-mechanisms-outsourced-data-cloud-2/",
"https://projectideas.co.in/building-confidential-efficient-query-services-cloud-rasp-data-perturbation/",
"https://projectideas.co.in/balancing-performance-accuracy-precision-secure-cloud-transactions/",
"https://projectideas.co.in/secure-data-retrieval-decentralized-disruption-tolerant-military-networks/",
"https://projectideas.co.in/product-aspect-ranking-applications/",
"https://projectideas.co.in/typicality-based-collaborative-filtering-recommendation/",
"https://projectideas.co.in/panda-public-auditing-shared-data-efficient-user-revocation-cloud/",
"https://projectideas.co.in/identity-based-distributed-provable-data-possession-multicloud-storage/",
"https://projectideas.co.in/control-cloud-data-access-privilege-anonymity-fully-anonymous-attribute-based-encryption/",
"https://projectideas.co.in/secure-dynamic-multi-keyword-ranked-search-scheme-encrypted-cloud-data/",
"https://projectideas.co.in/cloudprotect-managing-data-privacy-cloud-applications/",
"https://projectideas.co.in/secured-cost-effective-multi-cloud-storage-cloud-computing/",
"https://projectideas.co.in/ensuring-data-storage-security-cloud-computing/",
"https://projectideas.co.in/fuzzy-keyword-search-encrypted-data-cloud-computing/",
"https://projectideas.co.in/developing-secure-social-healthcare-system-cloud/",
"https://projectideas.co.in/access-control-mechanisms-outsourced-data-cloud/",
"https://projectideas.co.in/cloud-data-protection-masses/",
"https://projectideas.co.in/dynamic-bandwidth-allocation-cloud-computing/",
"https://projectideas.co.in/defenses-large-scale-online-password-guessing-attacks-using-persuasive-click-points/",
"https://projectideas.co.in/efficient-privacy-preserving-range-queries-encrypted-data-cloud-computing/"

]

for url, proj in zip(links, CloudProjects):
    proj['URL']= url

print(len(links)) #29
print(len(CloudProjects)) #29

# print(CloudProjects[4])
from utils import write_selected_dict_values_to_file

write_selected_dict_values_to_file(CloudProjects, 'CloudProjects.txt')