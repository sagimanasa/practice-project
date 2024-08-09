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
angular.module('marksApp', [])
  .controller('marksCtrl', function($scope, $http) {
	$scope.newmarks = {};
	$scope.marksList =[];
	$scope.domain="http://localhost:8000/"
	//$scope.domain="http://192.168.56.1:8000/"
	
	$scope.initialization = function(){
		$scope.getMarks();
		$scope.listenerInit();
	}
	
	
	$scope.updateform= function(marks){	
		$scope.updatemarks={}
		$scope.updatemarks.std_id=marks.std_id; 
		$scope.updatemarks.id=marks.id; 
		$scope.updatemarks.subject=marks.subject; 
		$scope.updatemarks.marks=marks.marks; 		
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
	
	$scope.getMarks = function() {
		console.log("##")
      $http({  
            url: $scope.domain + "marks",  
            dataType: 'json',  
            method: 'GET',    
            headers: {  
                "Content-Type": "application/json"  
            }  
        }).then(function (response) {   
            $scope.marksList = response["data"]["records"]; 		
        },function (error) {  
               console.log(error);  
         });  
    };
	$scope.addMarks = function(marks) {
		
	  $http.put($scope.domain + "marks", JSON.stringify(marks), {
		  headers: {  
                "Content-Type": "application/json"  
            }
		}).then(function (response){
			$scope.getMarks(); 		
        },function (error) {  
               console.log(error);  
        });  			  
    };
	$scope.updateMarks = function(marks) {
		console.log("##")
	   $http.post($scope.domain + "marks/"+marks.marks_id, JSON.stringify(marks), {
		  headers: {  
                "Content-Type": "application/json"  
            }
		}).then(function (response){
			$scope.getMarks(); 		
        },function (error) {  
               console.log(error);  
         });
    };
	$scope.deleteMarks = function() {
		console.log("##")
		url=$scope.domain + "marks/"+$scope.deletemarks_id
		
		$http({
		    url:url,
			method: 'DELETE'
	    }).then(function (response){
			$scope.getMarks();
		},function (error) {
			      console.log(error);
		 }); 
    };
	
  });
  
  
  