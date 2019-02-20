***Python Developer Workbook - Task 5***

1. Define the following terms and state why they are important in the relating to the planning phase of securing a network: 
- security model
	A security model is a framework from where security policies are developed, specified and enforced. The security model is implemented through policy, and can be on the basis of a formal model, or no theoretical grounding. The model aims to precisely define the level of implementation of security requirements. This is accomplished through linking the important aspects of security with their relationship with system behaviour. Essentially, it provides the blueprint that properly defines the security levels of network devices, operating systems, hardware, protocols and applications that can contain security vulnerabilties that can affect the system and the environment as a whole.

	In definition, a security model is a statement that outlines the requirements to properly implement certain security policies. A security model is important because it forms the foundation of implementing a secure system. Without it there will be a lack of cohesion and system-wide implementation of security, causing servers to be susceptible to attack.

- threat model
	A threat model is the active process in the security development process that identifies potential risks and threats, both internally or externally, and creates appropriate tests and countermeasures with the focus on responding to these potential threats. In cyber security, as the industry is constantly evolving, so too does the creation of threat models to accurately respond to emerging threats. To implement a successful threat model it is essential to identify potential threats, analyze these effects, determining the significance and find the appropriate counter-strategy.

	A threat model is important because an offensive, proactive strategy to security can allow the detection of possible intrusion pathways early, thus counter-measures can be timely adopted.

2	Define the following terms and state why they are important in terms of the building phase of securing a network: 
- security policies 
	Security policies are the primary element that in a successful implementation of security requirements. A security policy will set the ground rules in every organisation in regards to the level of security for each piece of infrastructure. A policy can be concerned about data access requirements, the level of security that is required for different systems, and the procedures and actions that are required when such requirements are not met.

	The security model and security policy are closely intertwined. A security policy can be about authentication and access control rights, and the security model will outline the logic and rules that should be implemented to ensure that no lower level users can have access control to higher level objects, for example.

	Security policies are important in securing a network because they are rulesets that are to be followed by the personel in the organisation. Proper following of guidelines can determine what a service can and cannot do, allowing for detection of anything that is beyond the extraordinary.

- security templates

	Security templates are templating files that are used to organise, configure, manage security on computers. These are otherwise known as a collection of security configuration settings that are applied to the domain controller, member servers or a workstation. The templates for security can be applied to a single workstation, or in Group Policy that affects a range of users. In Windows, the security templating and configurations are within the Active Directory. The advantages of security templating for improved efficiency and reduction of repetition, as templates can be directly imported to a new computer in the network. It is therefore possible to manage multiple computers in scale.

	Security templates are important because of reusability, and allows more efficient implementation of security policies.

3	Define the following terms and state why they are important during the managing phase of securing a network:
- network monitoring 
	Network monitoring is the systematic effort of patrolling system-wide traffic and components. Monitoring allows for the detection of slow or failing network components, such as server-side issues, router and switch problems and other device issues. It is a subset of network management, where all problems that are alerted are directed to the Network Administrator. Network monitoring is accomplished through the use of programs that help detect outages and other trouble. This is different to the intrusion detection system.

	An example would be to determine the sufficient functionality of a HTTP server, the software can periodically send a request packet to determine if there are any issues with the service. For mailing services, an SMTP message can be sent and received by IMAP and POP3. 

	It is important for the management phase of securing a network, because networks require constant attention and any changes should be met with a reasonable action. Having network monitoring allows for rapid response to unusual behaviour, and appropriate measures are implemented.

- security policy enforcement

	Security policy as aforementioned forms the basis of an organisation's information security. It is common and necessary that adequate security policy is in place to ensure information security. However it is insufficient to only have security policies but also achieve policy enforcement and compliance. Security policy enforcement is focused on teaching and educating users on the importance of security and the necessity of proper security focused conduct. Enforcement is tied with a program to educate, such as notifying of the existence of policy, complying with the policy, and consequences of non-compliance.

	The security policy enforcement is very important because all tasks are eventually carried out by human users. If there is a lack of enforcement, it doesn't matter how sophisticated the policy is because there will be no implementation of it anyway.

4	Describe TWO common types of ICT networks and why they are used and identify the hardware required to implement them. 100 - 200 words

	LAN (Local Area Network): A local area network is a computer network that is usually located in a single room or a small building. It consists of several computers and resources such as printers and scanners that are interconnected. The hardware that is required to implement LAN are usually ethernet cables. LAN is used because it allows for computers on the LAN to share resources and share and access information. 

	WLAN (Wireless Local Area Network): A wireless local area network is a computer network that is similar to LAN but instead of using cable hardware, uses Wi-Fi technology for intercommunication. Routers and wireless switches are used to communicate, send and receive data using wireless adaptors. It is physically safer than LAN because there are no cables. The point of a WLAN is the same as a LAN, and allows computers to share information together.

5	Describe TWO auditing and TWO penetration testing techniques.	250 - 300 words

	Security Auditing:
	1. Vulnerability Scanning: Vulnerability scanning is an inspection of potential exploitable aspects of computers or networks. It detects vulnerabilities and weaknesses in these systems that may arise by using active tools that attackers can also have access to. It allows organisations to gauge the extent of its security vulnerabilities and the likeliness of being exposed externally. Within vulnerability scanning there are several categories, such as network enumerator, which retrieves information about users and groups on networked computers.

	2. Network Scanning: The use of network scanning tools verifies connectivity between host and organisation networks, which provides a complete list of everything that is active in a system. Through network scanning it is possible to verify unauthorized network connections, services and collect evidence for forensics. Network scanning undergoes a procedure of identifying active hosts on a network. Some examples of network scanning will be through the use of the automated network scanning tool nmap, and can be used to scan for ports and enumerate them, or to conduct ping sweeps to discover available servers on the network.

	Penetration Testing:
	1. Manual: A manual approach of penetration testing uses non-automatic tools that focus on enumerating and exploiting by themselves. This can include nmap scans and visiting the website to find vulnerabilities, and creating and developing exploits for use. Manual penetration testing may not be scalable in the way that automated scans are, but many vulnerabilities require manual testing to be able to verify and successfully exploit the situation.

	2. Automatic: An automatic approach of penetration testing 
	uses pre-built software that conducts vulnerability scans, and then the penetration tester will look and interpret each vulnerability individually. They are generally automated software which intend to provide an affordable solution to the counterpart, which is often more expensive.

6	Describe how you would approach the analysis of logs and how these could assist investigation of security related networking matters. 100 - 200 words

	The analysis of log files is a complicated process. The best approach to analyse log files is to use log analysis tools such as splunk to help extract data from log files and find trends and patterns that will ultimately help guide general security. The pattern detection allows filtering messages to find relevant security issues, and correlation analysis can help detail a particular event(s). This can both assist the future planning of security, but also assist in preventing attacks that occur while it is happening. 

7	Describe TWO elements of network infrastructure common to all organisations from the list below: - routers - switches - cabling - gateway. 100 - 200 words

	- routers: A router is an appliance that facilitates the transferral of information between computer networks. The router serves as a gateway which is between where two networks or more intersect. The router aims to analyse a packets destination IP address, and finds the best and most efficient method to forward it to the recipient. Routers are situated on the OSI model network layer, since they are responsible for connecting machines via the internet protocol.

	- switches: A switch enables network connected devices to be able to communicate more efficiently. It is used in the data link layer (layer 2 of the OSI model) and helps to use hardware addresses (MAC) to connect, process and forward data at a lower level. The most common form of swtiches are for the ethernet.

8	Describe the purpose and capabilities of TWO software and TWO hardware network security solutions. 200 - 300 words

	Software network security solutions
	- Antivirus software (e.g. Avast): Antivirus software is a software network security solution that serves to protect systems, servers and devices by matching incoming traffic and files with recorded list of vulnerabilities that is frequently updated. Antivirus can be deployed that is network wide.

	- Software Firewall: A software firewall is software that is installed on the computer that has internet connection. These are cheap and easy to install, but may have problems related to compatibility and conflicts with other programs that is installed.

	Hardware network security solutions
	- Hardware Firewall: Hardware firewalls are generally devices that are placed between the router and internet connections. These are dedicated security devices which are optimised to carry out firewall duties. They are designed solely for firewall purposes, and thus do not weigh down on resources of personal computers.

	- PASS

9	Explain the role of the following concepts in terms of the processes and techniques of object-oriented programming: (250 - 350 words)
- abstraction 

	Abstraction is the act of removing characteristics and reducing something to a set of essential characteristics. This is used to reduce the complexity of the creation of an object, and thus increase the efficiency of the object. A method that a programmer can do is to name entities in a manner that has all the practical and useful elements included, and none of the non-essential ones.

- inheritance 

	Inheritance is a mechanism of allowing creating another class that share the same set of attributes and methods. Classes can be distinguished between sub, super, parent and child classes. An object class can inherit all of the information from the parent class. This allows the speeding up of program development,but also ensures that the newly created class is valid and working.

- polymorphism

	Polymorphism is the ability of presenting the same interface in various different forms (such as data types). Using polymorphism, each class will have the same identical underlying data, and each class can share the same attributes and methods, which all represent the behaviours that each have in common. An example is that there are many different shape classes, such as squares and circles, which are inherently different, but can have the same method draw().

- separation of concerns

	The separation of concerns is the principle of separating a computer program into sections, with each section 'concerned' about a specific issue. This is a form of abstraction because it simplifies the code to allow it greater efficiency.

10	Describe the process for developing: (150 - 250 words)
- small-size applications 

		Small-sized applications require less planning and can be accomplished with a single or several developers. There are limited amounts of code required for a fully functional product, and thus small sized applications are easy and efficient to create. This also means that there aren't as many functionalities, and most programs achieve the minimal viable product (MVP).

- large-size applications	

		Large-sized applications usually require a team of developers and contains a larger repository of code. These applications take a long time to build, and are maintained in github or other private repositories for efficiency between coders. There will usually be a lot of functionalities, and most programs can become commercial viable if they are client facing.

11	Identify and outline the key features of a graphical user interface (GUI), for interaction with an operator. 150 - 250 words

	PASS

12	Describe the architecture of a framework for web-enabled application development. 150 - 200 words

	Web application architecture is the interaction between the application, middleware that connects application, and the database so that they can seamlessly work together. In web-enabled application development there exists a server and client. The server has code that responds to incoming HTTP requests, whilst the browser code contains responses to user input. An example of web-enabled application development framework is Flask Python. Flask is a micro web framework built on Python. It has pre-existing libraries for common functionalities and extensions. Flask is generally used with MongoDB. The underlying components of Flask use a utility library Werkzeug, which is a toolkit for Web Server Gateway Interface applications.

	Flask has many features, including devlopment servers and debuggers, support for unit testing, secure cookies in client side sessions, extensive documentation and google search compatibility. These elements of the Flask framework allow for efficient web application development, and websites such as LinkedIn and Pinterest use this framework for web development.

	The application development generally undertake the MVC (Model View Controller) pattern. It separates the application logic into three separate parts, which allow for ease of collaboration and reuse. Model defines data structure through the use of databases. View is the general display and user interface, and the controller is the logic that connects the database with user interactions.

13	Outline the techniques for implementing inter-process communication 150 - 250 words

	Interprocess communication is a set of programming interfaces that allow for the coordination of activities running concurrently in an operating system. This can allow a single program to accept and handle multiple requests at the same time. As multiple processes can be the result of a single request, and that there are many requests, the processes are required to communicate with each other. Thus there are IPC methods:

		Pipes: A pipe is a technique that allows the passing of information from one program process to another. Pipes are a one-way form of communication. A pipe allows for the output or result of one process to be passed on or "piped" to the next process and so on. This can be demonstrated using the (|) symbol.

		Named Pipes: Named pipes are the same as pipes in that they pass information from one computer process to another through a pipe or message holding. Named pipes can be used by any process, and do not need to share the same origin process. Any messages sent can only be read by authorized processes that know the name of the named pipe.

		Other techniques include: message queueing, semaphores, shared memory and sockets.

14	Identify and outline testing techniques as applied to distributed application development. 200 - 250 words

	Base Testing: Distributed application development should be tested for their overall functionality. In distributed applications each service interface must be tested to determine the functionality of the entire product. The API functionality test should cover all aspects of the services, such as determining if the program will operate correctly if a correct user input is supplied. Rather than concentrating a single service, it concentrates on the overall application functionality.

	Scale Testing: Distributed applications are more complex in functionality and how they flow through the various services. Different paths may be triggered across a number of services. Each call in a distributed application may travel through a network, which means that response times may be the result of traffic on the network.

	Resilient Testing: Distributed application generally better address the application response to highly spontaneous user traffic. Individual servers that are part of the distributed application network can encounter failures, and thus they program must be resilient to infrastructure failures. The evaluation of these resilience should not be measured during heavy load, however.

15	Identify and outline techniques for implementing third-party supplied code. 200 - 250 words

	Manage and assess risks associated with thid party code: code libraries that were developed and used from either open source projects or outsourcing organisations have underlying security risks. An important strategy to maintaining a high level of security whilst utilising third party code is through perofmring code-level analysis, finding vulnerabilities in the code base before implementation. The code must be subjected to the same level of security verifications, and shouldn't be trusted without security testing.

	Alternatively, it is important to pay close attention to several aspects of the project before implementing the code in your system. Consider whether the project is well maintained and subject to frequent updates. Notice the general attitude of the community, and whether it has a large development team. Most importantly when implementing third party supplied code is to consider whether or not these libaries or codes are needed, or if they can replaced with a much simpler solution.

16	Describe the basic principles of database management systems.	150 - 250 words

	A DBMS is a system software for creating and managing databases. These systems create a systematic and logical method to manage data. A DBMS manages data, the database engine from which data is accessed, and the schema, which is the database logical schema. It allows for a centralised view of data, which can allow access of information by multiple users, in various locations. DBMS can be restrictive and limit what users can see depending on their rank, allowing different views of the same database schema. Database management systems can also allow for independence of physical data and logic. Applications can thus be protected from attackers who find the physical data, by using logic to conceal or maintain the database system.

	Relational database management systems, such as SQL-based databases, have a unified and standard programming language which allows for defining, protecting and accessing data.

	Thus there are many advantages of a DBMS. Some examples include additional data security from structured management, data abstraction and independence, the separation of physical and logic, and the ability swiftly recover from crashes and errors.

17	Outline the software development life cycle (SDLC) 100 - 150 words

	The Software Development Life-cycle (SDLC) is the process for companies to develop software with the highest quality and greatest efficiency, by clearly defining the stage the program is in within the life-cycle. There are multiple different models of SDLC, some of which include the Agile and Waterfall frameworks. The SDLC life-cycle can be separated into separate stages, as mentioned below:

    - Identification and Planning Stage: This is the preliminary stage where a problem is identified, which is usually tied to the wants or needs of the customer and other stakeholders. Planning will usually involve the initial determination of the costs and resources that are required to complete the project. It also involves risk and cost-benefit analysis in creating a program.

    - Architectural and Analysis Stage: What is regarded as the most important stage, the initial plans are converted into actual coding design, and a Design Specification is created. A competent plan and design is responsible for managing costs and project deadlines.

    - Construction and Designing Stage: This is the stage where the developers are responsible for the creation of the program. 

    - Test and Debugging (Implementation) Stage: The program is refined through various testing and debugging. The issues are continuously fixed until it reaches the quality of the initial specifications.

    - Deploying and Maintenance Stage: The program is launched, and adjustments are regularly made throughout time to further improve the program going into the future.

    - Evaluation Stage: The development team considers and evaluates the program and the development, as well as any issues that have occurred. This will help them in future endeavours of a similar nature, or with the same team.

18	Explain the coding used to create deployment applications. 150 - 250 words

	A deployment application is a script or software that is created for the sole purpose of installing a program onto a server. Generally when initiating the deployment application, the code will download the file, or if it's already downloaded the program, extract and install it into the application folder on the operating system. Where dependencies are required, the installation script will either abort until the user can fix and update the missing installations, or install the dependencies themselves. Most of the time the deployment application will refer to code from within the main application. This is known as the activation phase, where it will execute the main components of the software for the first time, where an installation wizard can be employed to install the application to the respective folders. Licensing and other options are also concerned.

19	Describe the design pattern used to implement remote procedure calls in the application you created in Task 3.	150 - 250 words

	PASS

20	Explain the information and communications technology (ICT) hardware, software, security protocols and standards and organisational policies relevant to deployment of applications.	150 - 250 words

	PASS


