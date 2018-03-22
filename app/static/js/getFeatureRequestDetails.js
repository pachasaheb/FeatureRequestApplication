//On featureRequestDeatils.html load using ajax() get reqeust we will retrieve Json data from retrieveFeatureRequestManager function present in featurerequestmanager.py 
//After getting Json data it prints Json data to html
$(document).ready(function(){
    $.ajax({
        url: '/retrieveFeatureRequest',
        type: 'get',
        dataType: 'json',
        success: function(data){
            console.log("json"+data.details);
            // Prints the retrieved JSON data into a table
            $('#FeatureRequest_table').DataTable({
                pageLength: 5,
                lengthMenu: [ 5,10, 25, 50, 75, 100 ],
                responsive: true,
                data: data.details,
                columns: [
                    {
                        'data': 'title',
                        "render": function (data, type, row) {
                            if (type === 'display') {
                                // Returns title as a hyper link to click on and modal gets displayed and on click returns the Feature Request details of particular row
                                return '<a data-toggle="modal" data-target="#UpdateModal" onclick="OnClickTableRow(\''+ row['title'] +'\',\''+ row['description'] +'\',\''+ row['client'] +'\',\''+ row['clientPriority'] +'\',\''+ row['targetDate'] +'\',\''+ row['productArea'] +'\')">' + data + '</a>';
                            }
                            return data;
                        }
                    },
                    { 'data': 'description' },
                    { 'data': 'client' },
                    { 'data': 'clientPriority' },
                    { 'data': 'targetDate' },
                    { 'data': 'productArea' }
                ]
            });
        }
    });
});

// When a particular row is selected in table of Feature Request details all the row values are passed to OnClickTableRow funciton
function OnClickTableRow(tableTitle,tableDescription,tableClient,tableClientPriority,tableTargetDate,tableProductArea){
var tableDate=new Date(tableTargetDate);
tableTargetDate = tableDate.getMonth()+1 + "/" + tableDate.getDate() + "/" + tableDate.getFullYear();
console.log("Inside data table"+tableTitle);
// FeatureRequestFormUpdateModel acts as binding model for update modal 
function FeatureRequestFormUpdateModel() {
    title = ko.observable(tableTitle),
        description = ko.observable(tableDescription),
        client = ko.observable(tableClient),
        clientPriority = ko.observable(tableClientPriority),
        targetDate = ko.observable(tableTargetDate),
        productArea = ko.observable(tableProductArea)

};
// On modal-close page is reloaded to flush out values present in modal
$("#modal-close").click(function(){
    window.location.reload();
});
// knock out js has applyBindings property which will apply the binding of model on filling data
ko.applyBindings(new FeatureRequestFormUpdateModel());
};
// onUpdate function is used to post the updated feature Request details to http://127.0.0.1:5000/editFeatureRequest 
onUpdate = function () {
    console.log("inside update")
    $.ajax({
        data: JSON.stringify({
            title: title(),
            description: description(),
            client: client(),
            clientPriority: clientPriority(),
            targetDate: targetDate(),
            productArea: productArea()
        }),
        type: 'POST',
        url: '/editFeatureRequest',
        contentType: 'application/json',
        success: function (result) {
            if(result == 'success') {
                window.location.reload();
            }
            else { alert("Please Check your values and Submit"); }
        },
        error: function (error) {
            console.log(error);
            alert("Please check your details and resubmit" + error)
        }
    })
};
