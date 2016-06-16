<!DOCTYPE html>
<html lang="en">
	<head>
	 	<meta charset="utf-8">
	 	<title>To Do List | Python Practice No. 3</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">

		<!-- Loading Bootstrap -->
		<link href="/static/css/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">


		<!-- Loading Flat UI -->
		<link href="/static/css/flat-ui.min.css" rel="stylesheet">
		<link href="/static/css/style.css" rel="stylesheet">
		<link rel="shortcut icon" href="/static/img/favicon.ico">
		<link href="/static/style.css" rel="stylesheet">
		<!-- HTML5 shim, for IE6-8 support of HTML5 elements. All other JS at the end of file. -->
		<!--[if lt IE 9]>
			<script src="js/vendor/html5shiv.js"></script>
			<script src="js/vendor/respond.min.js"></script>
		<![endif]-->
	</head>

	<body>
 	<div class="container">
		
		<div class="col-xs-2"></div>
		<div class="col-xs-8" style="background: white">

		<center>
			<h1 class="full-block">SIMPLE TO-DO LIST</h1>
			<label class="text_label">Click The Pencil Icon to Edit Me</label><div class="edit"></div>
			<input type="text" class="for-edit" value="Click The Pencil Icon to Edit Me" />
			<div class="clear"></div>
		</center>
		<br />
		  
		  <form id="form-todo-list">
		    <div id="todo-list" class="todo-list">
		    
		    </div>

		  </form>

  		<form id="form-add-todo" class="form-add-todo">
		    <label for="todo"></label>


		    <div class="input-group">
			    <input type="text" id="new-todo-item"  class="form-control new-todo-item" name="todo" placeholder="What are you doing to do today?">
					<span class="input-group-btn">
						<button type="submit" id="add-todo-item" class="btn add-todo-item">
					  		<span class="fui-plus"></span>
						</button>
			 		</span>
			 </table>
		 	</div>

		  </form>

		  <br />
		  <br />
  	</div>
  	<div class="col-xs-2"></div>		
 	</div><!-- /.container -->

 	<div class="container">
 		<footer>
    	<center>
    		<small>
    			Created and developed by <a href="https://mage-isdcs.slack.com" target="_blank">mage-isdcs</a>.
    		</small>
    	</center>  	
  	</footer>
	</div>
	</body>
	<script type="javascript">
		$(':checkbox').radiocheck();
	</script>
	<!-- jQuery (necessary for Flat UI's JavaScript plugins) -->
	<script src="/static/js/vendor/jquery.min.js"></script>
	<!-- Include all compiled plugins (below), or include individual files as needed -->
	<script src="/static/js/vendor/video.js"></script>
	<script src="/static/js/flat-ui.min.js"></script>

	<script type="text/javascript" src="/static/jquery-1.4.2.min.js"></script>
	<script type="text/javascript" src="/static/easy-editable-text.js"></script>

	<script type="text/javascript">




			function addTodoItem() {




			  var todoItem = $("#new-todo-item").val();
			  $("#todo-list").append("<label class='checkbox'><input type='checkbox'" + 
			                         " name='todo-item-done'" + 
			                         " class='custom-checkbox todo-item-done' data-toggle='checkbox' id='checkbox'"+ 
			                         " value='" + todoItem + "' /> <span class='icons' style='font-size: 23px'><span class='icon-unchecked'></span><span class='icon-checked'></span></span><span class='todo-text'> " +
			                         "</span><button class='btn btn-xs btn-danger todo-item-delete'>"+
			                         "<span class='fui-cross'></span></button><button id='editable'>E</button><img src='/static/space.png'>"+ 
			                         todoItem +
			                         " <hr /></label>");
			 
			 $("#new-todo-item").val("");



			}

				


			function deleteTodoItem(e, item) {
			  e.preventDefault();
			  $(item).parent().fadeOut('slow', function() { 
			    $(item).parent().remove();
			  });
			}

			                           
			function completeTodoItem() {  
			  $(this).parent().toggleClass("strike");
			}


			$(function() {
			 
			   $("#add-todo-item").on('click', function(e){
			     e.preventDefault();
			     addTodoItem()
			   });
			  
			//EVENT DELEGATION
			//#todo-list is the event handler because .todo-item-delete doesn't exist when the document loads, it is generated later by a todo entry
			//http://learn.jquery.com/events/event-delegation/
			  $("#todo-list").on('click', '.todo-item-delete', function(e){
			    var item = this; 
			    deleteTodoItem(e, item)
			  })
			  
			  $(document).on('click', ".todo-item-done", completeTodoItem)

			});


	</script>

</html>