
## Task Overview

-   [Part 1] Create a REST API and deploy it on any cloud service.
    
    API Specifications:
    
    -   The API should take only one parameter called `name` as input and returns a string wishing happy birthday that uses the value in the name parameter as output.
    
    e.g., if the value of the `name` parameter is Elon Musk, then API returns _“Happy Birthday,_ Elon Musk*!”*
    
    You have to share these with us. Keep these with you, and move on to the next part of the task. The last section of this document contains instructions on how to share it with us.
    
    1.  Share the URL of the API deployed on the cloud.
    2.  Share the git repo URL with the code for the API.
    3.  Share the API documentation in OpenAPI2.0 format. (.JSON or .YAML) Refer: [](https://swagger.io/specification/v2/)[https://swagger.io/specification/v2/](https://swagger.io/specification/v2/)
-   [Part 2] Now that the API is ready, build the following workflow using a no-code platform called Zapier.
    
    1.  Retrieve the list of objects in the following format using [t](https://ab-solution-engineer-task.s3.ap-southeast-1.amazonaws.com/list.txt)he API (link is provided below).
        
        ```json
        {
          "name": "Elon Musk",
          "email": "elon@spacex.com",
          "image": "link to image"
        }
        {
          "name": "Jeff Bezos",
          "email": "jeff@blueorigin.com",
          "image": "link to image"
        }
        
        ```
        
        **Link:** [](https://ab-solution-engineer-task.s3.ap-southeast-1.amazonaws.com/list.txt)[https://ab-solution-engineer-task.s3.ap-southeast-1.amazonaws.com/list.txt](https://ab-solution-engineer-task.s3.ap-southeast-1.amazonaws.com/list.txt)
        
        Do not copy-paste the content from the link. This data must be retrieved from the link when the flow is executed.
        
    2.  For each object in the list, get the string by passing the `name` of the object to the API that you built in Part 1
        
        e.g., If the name is Elon Musk, and email address is [elon@spacex.com](mailto:elon@spacex.com). Use the name “Elon Musk” to get the string “Happy Birthday, Elon Musk!” from the API you built in Part 1.
        
    3.  Send an email that contains the **string** and the **image** to the email address specified in the object. The email body must contain the string, and the subject should be "Wishes"
