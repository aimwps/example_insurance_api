$(document).ready(function(){
  $(document).on("click","button[name='launch_process_csv_modal']", function(e){
    console.log("registered")
    e.preventDefault();
    $("#processCsvModal").modal("toggle")
  })
})
