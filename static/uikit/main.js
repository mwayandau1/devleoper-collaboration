    let searchForm = document.getElementById('searchForm');
    let pageLinks = document.getElementsByClassName('page-link')
  
    if(searchForm){
      for(let i=0; pageLinks.length > 1; i++){
        pageLinks[i].addEventListener('click',function(e){
          e.preventDefault();
          //Get the data attr
          let page = this.dataset.page
            //Add hidden search input to form
          searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

          //Submit the form
          searchForm.submit()
        })
      }
    }

