$(document).ready(function(){
  function displayFinalExitStatus(json){
    console.log(json)
      if(json.complete == true){
        $("#submitDocument").removeClass("disabled")
        displayExitStatus(`${json.quantity_to_add}. Click proceed to continue`)

      } else {
        $("#submitDocument").addClass("disabled")
        displayExitStatus("One or more fatal errors is preventing this document from upload. It will now be deleted.")
      }

  }
  function displayRemainingErrors(json){
    $("#age_info").empty()
    $(json.age.errors).each(function(i, message){
      $("#age_info").append(`
        <li class="list-group-item">
        ${message}
        </li>`
      );
    });

    $("#gender_info").empty()
    $(json.sex.errors).each(function(i, message){
      $("#gender_info").append(`
        <li class="list-group-item">
        ${message}
        </li>`
      );
    });

    $("#BMI_info").empty()
    $(json.bmi.errors).each(function(i, message){
      $("#BMI_info").append(`
        <li class="list-group-item">
        ${message}
        </li>`
      );
    });

    $("#children_info").empty()
    $(json.children.errors).each(function(i, message){
      $("#children_info").append(`
        <li class="list-group-item">
        ${message}
        </li>`
      );
    });

    $("#region_info").empty()
    $(json.region.errors).each(function(i, message){
      $("#region_info").append(`
        <li class="list-group-item">
        ${message}
        </li>`
      );
    });

    $("#smoker_info").empty()
    $(json.smoker.errors).each(function(i, message){
      $("#smoker_info").append(`
        <li class="list-group-item">
        ${message}
        </li>`
      );
    });

    $("#expenses_info").empty()
    $(json.expenses.errors).each(function(i, message){
      $("#expenses_info").append(`
        <li class="list-group-item">
        ${message}
        </li>`
      );
    });

}
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
          displayRemainingErrors(json)
          displayFinalExitStatus(json)
        }
      }
    })
  }
  function addCheckedDataToDatabase(documentId){
    $.ajax({
      type: "POST",
      url: "/ajax_add_checked_document/",
      data: {csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            document_id: documentId},
      datatype: 'json',
      success: function(json){
        window.location = "/uploads/"
        alert("Upload succesful, Explore the API to see the new entries")

      }
    })
  }
  $(document).on("click","#launch_process_csv_modal", function(e){
    console.log("registered")
    e.preventDefault();
    $("#processCsvModal").modal("toggle")
    let documentId = $("#select_unprocessed").val();
    $("#submitDocument").val(documentId)
    getDocumentStatus(documentId);
  })
  $(document).on("click", "#submitDocument", function(e){
    e.preventDefault()
    let documentId = $(this).val()
    addCheckedDataToDatabase(documentId)
  })





})
