# Threat Model

Edit: Our network security teacher responded to the threat model, and further edits are added to improve on the quality of the report.

***The common and emerging vulnerabilities for client***

The client is a tech-savvy senior executive who is an early adopter of new technologies. Since these technologies have yet to mature, many of the client's vulnerabilities are gadget and network security related. From a technical perspective, it seems that there are extended antennas attached to the router that exceed the necessity of the household, and into the street front. The owner also has several mobile devices, and depending on the firmware and frequency of updates, can be insecure and vulnerable to someone on the same network. The same situation applies to the computers, and especially because it is running Windows 8.1, which has several new vulnerabilties that allows for remote code execution and buffer overflows. 

Furthermore, there are concerns with adopting technology such as Internet of Things. As they are relatively recent and undertested, vulnerabilities can emerge, especially since the family has many different devices that are interconnected through a web GUI. The family also has two Grandstream products, namely the Grandstream GVC3200, which is a video streaming camera that allows for business conferences, and the GAC2500, which is a audio conferencing phone device. These products are also vulnerable to several common exploits, such as XSS, CSRF and SQL injections.

Edit: A common vulnerability for Windows 8.1 is the CVE-2018-8453 that allows for privilege escalation where the win32k fails to handle objects in a memory. An emerging vulnerability for Windows 8.1 are CVE-2019-0575 - CVE-2019-0584. These vulnerabilities are released in early 2019, and can cause a remote code execution vulnerability as a result of the improper handling of memory. 

***Attacker Profiling***

To better understand the attack pathways of a potential attacker, we will create several hypothetical profiles.

**First Profile: Business Adversary**
*The Business Adversary (BA) intends to gain knowledge about the competition through malicious means*

The attacker can be a simple 'friend' or colleague who has a malicious interest in gaining privileged knowledge about the company that the senior executive works for, most likely so that the information can provide business insights to a fellow rival company, or if the company is disliked for social/political/cultual reasons, to publically disclose information to damage their reputation. The attacker can also conduct such activities for personal gain, as business information can be sold for signficant capital windfall.

Since the attacker in this scenario is a friend, it is likely that s/he can access the house and its infrastructure during a visit. The attacker can install malicious software on a computer/device if the machine is `insecure`. If the attacker borrows the wifi password, s/he could later access the network outside of the house, due to the extended wifi signals, and use it to exploit the already vulnerable machines, thus granted him/her access to the devices and information.

The technical expertise would be moderate, since basic penetration testing skills would be required. The most important part to execute this would be to have a high level of interpersonal and social engineering skills.

If the attacker can successfully breach the system and gain access to the devices in the household, valuable business information stored on a computer/laptop/device can be accessed, and thus can cause serious repercussions to the company and individual.

**Second Profile: Impersonal Hacker - Neighbour**
*The Impersonal Hacker (IH) can be anyone, anywhere, who exploits devices that are connected to the interest for malicious reasons. In this circumstance, it can be a neighbour who has discovered vulnerabilities in the network and wants to breach it out of personal interest*

Edit: The attack can be anyone who discovers vulnerable machines connected to the internet. This can be either through visiting websites such as Shodan. The difficult part of tracking these people down is that they can be entirely unrelated to the client. Although the neighbour can be tracked down, it is difficult to know because the household might not know the intentions of the malicious neighbour, and what s/he wants to gain from this attack.

The attacker can discover a vulnerable IOT machine or Grandstream appliance online, and after brute-forcing or through exploiting vulnerabiltities, gain access to the device. There is no need for any physical proximity in this attack. The attacker can also physically invade the household, in an attempt to get the wifi password or steal an appliance for further brute force and cracking. The best way to access the home will be through the park behind the house, and this should therefore be secured.

The attack is highly sophisticated in order to exploit an IOT or other device, however if the security of these applicances are low then the attacker can easily bypass security.

An attacker can use exploited IOT machines or cameras to conduct further reconassiance on the target, or to use those machines as bots for other attacks etc.

***Categories of threats to consider***

The various threats that are previously identified can be categorised:

**Physical Threat**
The physical threat occurs because there is insecurity that allows access of infrastructure that should be exclusive to the family. From how the wifi can be accessed from beyond the boundaries of the property, to how visitors can access private information internally. 

**Network Threat**
If the attacker can access the same network as the owner, the devices on the same network can be vulnerable to attack. The HP laptops that are running Windows 8.1 are vulnerable to various types of RCE and buffer overflow, and a talented hacker can find methods to exploit and gain access to these systems. Similarly, Grandstream devices have XSS and CSRF vulnerabilties, and in combination with social engineering can be used to gain access as well.

**New Technology Threat**
Technologies such as IOT have many vulnerabilities that are yet to be discovered, and Shodan can allow for the discovery of these applicances. These should be considered since they are on the network, and can be used for maliious purposes.

**Infrastructure Threat**
The lack of physical infrastructure can be a threat to the household. There is a lack of phone home capability, which means the family has to rely on mobile phones for communication. The back fence adjoins a public park, which means physical attackers have an easier access. The wifi router is also located in a not-ideal position, and can easily be damaged in the process.

The security posture of the network and the household is insufficent. Whilst the household security resembles that of an ordinary household, there are more attackers that are willing and able to profit from this household in particular, primarily due to the nature of their employment positions. Therefore, more security is required in order to protect the household from external attackers that ordinary households might not need to consider.