
new Promise((resolve, reject) => {
    if (localStorage.getItem('apiToken') != null) {
      resolve(localStorage.getItem('apiToken'))
        $.ajax({
             url: 'http://localhost:8000/api/projects/',
             method: 'get',
             headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
             data: JSON.stringify({username: 'admin', password: 'admin'}),
             dataType: 'json',
             contentType: 'application/json',
             success: function(response, status){console.log(response);},
             error: function(response, status){console.log(response);}

        });

        $.ajax({
         url: 'http://localhost:8000/api/issues/',
         method: 'get',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         data: JSON.stringify({username: 'admin', password: 'admin'}),
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log(response);},
         error: function(response, status){console.log(response);}

        });

        $.ajax({
         url: 'http://localhost:8000/api/projects/2',
         method: 'get',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         data: JSON.stringify({username: 'admin', password: 'admin'}),
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log(response.issues_project);},
         error: function(response, status){console.log(response);}

        });

        $.ajax({
         url: 'http://localhost:8000/api/issues/',
         method: 'post',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         data: JSON.stringify({summary: "Issue_21", description: "Project of Emir", status: 10, type: 2,}),
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log(response);},
         error: function(response, status){console.log(response);}

        });

        $.ajax({
         url: 'http://localhost:8000/api/issues/15',
         method: 'delete',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log(response);},
         error: function(response, status){console.log(response);}

        });
    } else {
            $.ajax({
                url: 'http://localhost:8000/api/login/',
                method: 'post',
                data: JSON.stringify({username: 'admin', password: 'admin'}),
                dataType: 'json',
                contentType: 'application/json',
                success: function(response, status){localStorage.setItem('apiToken', response.token);},
                error: function(response, status){console.log(response);}
            }
        )
    }
  });
