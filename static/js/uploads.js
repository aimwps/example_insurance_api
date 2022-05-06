$(document).ready(function(){
  function displayExitStatus(exitMessage){
    $("#exit_status").empty()
    $("#exit_status").text(exitMessage)
  }
  function displayColumnErrors(errorMessages){
    $("#column_names_info").empty();
    $(errorMessages).each(function(i, message){
      $("#column_names_info").append(`
        <li class="list-group-item">
        ${message}
        </li>
        `)
      displayExitStatus("We cannot continue checking with incorect column names. The document has been removed from uploads. Please correct the column names and upload the document again")
    })
  }

  function getDocumentStatus(documentId){
    $.ajax({
      type: "GET",
      url: "/ajax_get_document_status/",
      datatype: "json",
      data: {document_id: documentId},
      success: function(json){
        if (json.column_names.complete == false){
          displayColumnErrors(json.column_names.errors)

        } else {
          $("#column_names_info").empty();
          $("#column_names_info").append(`
            <li class="list-group-item">
            Column names are all correct
            </li>
            `)
        }
      }
    })
  }
  $(document).on("click","#launch_process_csv_modal", function(e){
    console.log("registered")
    e.preventDefault();
    $("#processCsvModal").modal("toggle")
    let documentId = $("#select_unprocessed").val();
    getDocumentStatus(documentId);
  })





})
