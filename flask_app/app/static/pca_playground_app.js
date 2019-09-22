var pca_dims = {
    show:0,
    total:0,
    arr:[],
    updates_sent_to_server:false
};

function initPCAArr(){
    for(var i=0;i<pca_dims.total;i++){
        pca_dims.arr.push(0);
    }
    $('#pca_array').val(JSON.stringify(pca_dims.arr));
}

function submitToServer(){
    if(!pca_dims.updates_sent_to_server){
        $('#pca_array').val(JSON.stringify(pca_dims.arr));
        $('form#pca_dim_form').submit();
        pca_dims.updates_sent_to_server = true;
    }
}

function updateVal(field_index,new_value){
    pca_dims.arr[field_index] = new_value;
    pca_dims.updates_sent_to_server = false;
}

function attachListeners(){
    for(var i=0;i<pca_dims.show;i++){
        $("#pca_"+i).change({field_index:i},function(ev){
            updateVal(ev.data.field_index, ev.currentTarget.valueAsNumber);
        });
    }
}

function attachCssToResultsFrame(){
    $('#resultFrame').load(function(){
        console.log('test');
        var contents = $(this).contents();
        var head = $(contents).find("head");
        head.append($("<link/>", 
        { rel: "stylesheet", href: '/static/result_style.css', type: "text/css" }
        ));       
    });
}

document.addEventListener("DOMContentLoaded", function(){
    initPCAArr();
    attachListeners();
    submitToServer();
    setInterval(submitToServer, 3000);
    attachCssToResultsFrame();
});