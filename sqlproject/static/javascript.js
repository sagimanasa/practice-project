angular.module('userApp', [])
  .controller('userCtrl', function($scope, $http) {
    $scope.newstudent = {};
    $scope.studentList = [];
	$scope.domain="http://localhost:8000/"
	//$scope.domain="http://192.168.56.1:8000/"
	$scope.initialization = function(){
		$scope.getStudent(); 
		$scope.listenerInit();
	}
	$scope.updateform= function(student){	
		$scope.updatestudent={}
		$scope.updatestudent.std_id=student.std_id; 
		$scope.updatestudent.name=student.name;
		$scope.updatestudent.age=student.age; 
		$scope.updatestudent.gender=student.gender; 		
	}
	$scope.deleteform= function(std_id){	
		$scope.deletestd_id=std_id
	}
	$scope.listenerInit = function(){
		var exampleModal = document.getElementById('exampleModal')
		exampleModal.addEventListener('show.bs.modal', function (event) {
		  // Button that triggered the modal
		  var button = event.relatedTarget
		  // Extract info from data-bs-* attributes
		  var recipient = button.getAttribute('data-bs-whatever')
		  // If necessary, you could initiate an AJAX request here
		  // and then do the updating in a callback.
		  //
		  // Update the modal's content.
		  var modalTitle = exampleModal.querySelector('.modal-title')
		  var modalBodyInput = exampleModal.querySelector('.modal-body input')

		  modalTitle.textContent = 'New message to ' + recipient
		  modalBodyInput.value = recipient
		})
	}
	$scope.getStudent = function() {
      $http({  
            url: $scope.domain + "student",  
            dataType: 'json',  
            method: 'GET',    
            headers: {  
                "Content-Type": "application/json"  
            }  
        }).then(function (response) {   
            $scope.studentList = response["data"]["records"]; 		
        },function (error) {  
               console.log(error);  
         });  
    };
	$scope.addStudent = function(student) {
		console.log("##")
	  $http.put($scope.domain + "student", JSON.stringify(student), {
		  headers: {  
                "Content-Type": "application/json"  
            }
		}).then(function (response){
			$scope.getStudent(); 		
        },function (error) {  
               console.log(error);  
        });  			  
    };
	$scope.updateStudent = function(student) {
		console.log("##")
	   $http.post($scope.domain + "student/"+student.std_id, JSON.stringify(student), {
		  headers: {  
                "Content-Type": "application/json"  
            }
		}).then(function (response){
			$scope.getStudent(); 		
        },function (error) {  
               console.log(error);  
         });
    };
	$scope.deleteStudent = function() {
		console.log("##")
		url=$scope.domain + "student/"+$scope.deletestd_id
		
		$http({
		    url:url,
			method: 'DELETE'
	    }).then(function (response){
			$scope.getStudent();
		},function (error) {
			      console.log(error);
		 }); 
    };
  });
  