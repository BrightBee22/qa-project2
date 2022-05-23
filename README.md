# MH Rise Weapon Suggestor

## Table of Contents
* [Introduction](#intro)
* [Design](#design)
    * [Risk Assessment](#risk-assessment)
    * [Trello Board](#trello-board)
    * [CI Pipeline](#pipeline)
* [App Design](#app)
* [Ansible and Nginx](#anginx)
* [Automation and Testing](#testing)
* [Future Improvements](#future-improvements)
* [Final Thoughts](#final-thoughts)
* [Acknowledgements](#ack)
* [Presentation](#presentation)
* [Licensing](#lis)


## Introduction <a name="intro"></a>
Specifications for this project required an application with a service-oriented architecture, composing of 4 services working together using technologies learnt at the academy; Jenkins, Docker and Docker Swarm, Ansible, Git, Nginx and GCP Virtual Machines. Service 2 and 3 generating random objects, Service 1 getting those random objects and posting to service 4 and then Service 4 generating a response based on the objects generated from 2 and 3 - With all information being shown on a webpage from Service 1.

Based on these specifications, I had the idea to develop an app based on my favourite game "Monster Hunter Rise". Initially the idea was to have service 2 generate a monster and then generate a random monster part to get based on that. For service 3, a weapon would be generated and then a switch skills would be given based on the weapon generated. Basically acting as a quest generator that would determine what monster, weapon, target monster part to get and switch skills to equip.

The journey for the first app looked something like this.

![firstjour]

However, I realised I would need to make something much simpler and achievable within the time-limit. So I reworked this idea to instead take the objects generated from service 2 and 3 to suggest a weapon the user could equip based on the monster's weakness. Looking something like this.

![secondjour]

## Design <a name="design"></a>


### Risk Assessment <a name="risk-assessment"></a>

Risk Assessment Below:

![ra]

### Trello Board <a name="trello-board"></a>
To track my progress on the project I used a Trello board (screenshot below).
![trello]

The board allows elements created to be moved section to another easily, meaning they can be tracked from initial creation to completion in implementing.

* *Epic* - General idea of which the user stories will come from.
* *User Stories* - Functionality implemented into the project based on the user's perspective. Tasks are formed from these stories.
* *To Do* - Elements being considered for implementation in the project.
* *In Progress* - Elements that are currently being worked towards.
* *Done* - Any element that is considered to be finished 

### CI Pipeline <a name="pipeline"></a>

Below is the Continous Intergration Pipeline for the project.

![ci]


## App Design <a name="app"></a>
Application written for all services was written using Python, the front-end app design was done using Flask, with the virtual machine being hosted by GCP. Below is an image of the webapp.

![1app]

Another image of the web app to prove it's randomised.
![2app]

In terms of the actual coding, service 2 and service 3 generated an object based on a list I created for each service. Code was written to randomly select one of the objects from the list and set as the response for the service (image below).

![backend1]

![backend2]

As you can see each there are possibility of 5 objects that can be generated from service 2 and 3. As service 4 needed to produce an output based on those objects, my response from service 4 was written using an if function of all possible combinations of those objects. Image below.

![backend3]

Dockerfiles were written for each service to containerise the app and then using docker-compose.yaml, the images were built for each service container.

![backend4]


Coding was done using a feature-branch model where a functionality was developed on one branch and then once complete, pushed to the repo and merged with the dev branch, and finally merged with the main branch once ready for deployment.

## Ansible and Nginx <a name="anginx"></a>
Using Ansible, I configured two seperate Virtual Machines to a docker swarm and installed Docker and cloned the repo using ansible. Configuration of the virtual machines was done using the inventory.yaml and playbook.yaml.
![inventory]

![playbook]

I also configured an Nginx.conf to act as a load bouncer. Configuration of which can be seen below.
![Nginx]

## Automation and Testing <a name="testing"></a>
Using Jenkins Pipelines, I automated the building and pushing of my containers, the deployment and also the testing of which - all of which was written in a Jenkinsfile. 

![pipeline]

All stages of my Jenkins pipeline were successful coverage reports were produced from each service.

![pipeline2]

Service 1 coverage report:

![test1]

Service 2 coverage report:

![test2]

Service 3 coverage report:

![test3]

Service 4 coverage report:

![test4]

## Future Improvements <a name="future-improvements"></a>

For future improvements, I would like to add more monsters and weapons to the list for service 2 and 3, making a richer generator and more variables to produce results from. However due to the amount of written coding needed and the limits of my current knowledge, this is something I would implement at a later date when I have more knowledge of how to implement this in an efficient way.

Additionally, I would make the website more visually interesting. Changing the colour of the monster name or webpage based on the weakness of the monster and colour coding it. This way the website would look less bland.

I would also implement a database to store different weapons based on the element the monsters are weak to and call a random weapon based on the element instead of a static choice linked with the monster (which is currently hard-coded). This would add another layer of randomisation to the app as there are multiple weapons in the game that can be used.

## Acknowledgments <a name="ack"></a>
I would like to thank all the trainers at QA who guided and taught me the skills needed to develop this project, special thanks to Ryan Wright who oversaw this project in particular. 

I'd like to add, references to items and creatures from the game 'Monster Hunter' do not belong to me and all rights belong to CAPCOM.

## Presentation <a name="intro"></a>
Link to presentation: https://drive.google.com/file/d/1ibfOnKws87le-H7tbzYaVcnstW6AEio-/view?usp=sharing

## Licensing <a name="lis"></a>
   Copyright 2022 Afolabi Bright-Oridami

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.







[firstjour]:https://i.imgur.com/xIXpr6c.png
[secondjour]:https://i.imgur.com/sfjMpxF.png
[trello]:https://i.imgur.com/5tkMx8o.png
[1app]:https://i.imgur.com/gick4OE.png
[2app]:https://i.imgur.com/22MuoZw.png
[backend1]:https://i.imgur.com/CSSdM8g.png
[backend2]:https://i.imgur.com/QXfqozD.png
[backend3]:https://i.imgur.com/F1LdvSQ.png
[backend4]:https://i.imgur.com/sTO5Gck.png
[inventory]:https://i.imgur.com/pR0FIqy.png
[playbook]:https://i.imgur.com/dR3JCZV.png
[Nginx]:https://i.imgur.com/ESs1bU1.png
[pipeline]:https://i.imgur.com/Q5DB1Dy.png
[pipeline2]:https://i.imgur.com/VUAeCdI.png
[test1]:https://i.imgur.com/Gmbpk7t.png
[test2]:https://i.imgur.com/d6mguf8.png
[test3]:https://i.imgur.com/84nk0Tr.png
[test4]:https://i.imgur.com/RdiBbAh.png
[ra]:https://i.imgur.com/mFqiPx7.png
[ci]:https://i.imgur.com/B9KTAhh.png