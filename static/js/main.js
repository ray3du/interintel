/**
 * @Param {string} q : query string to be searched
 * */
const SearchFunction = async (q) => {
    const url = location.protocol + '//' + location.host + '?action=search_data&q=' + q
    console.log(url)
    return new Promise((resolve, reject) => {
        fetch(url)
            .then(res => res.json())
            .then(data => {
                resolve(data.results)
            })
            .catch((err) => {
                console.log("Error: ", err)
                reject([])
            })
    })
}

let state = {
    products: [],
    /**
     * @Param {Array} items
     * */
    setProducts: (items) => {
        state = {
            ...state,
            products: [...items]
        }
        state.renderItems()
    },
    renderItems: () => {
        const { products } = state
        let items = ''
        if(products.length > 0){
            products.forEach(product => {
                const product_detail_url =  location.protocol + '//' + location.host + '/product/' + product.id
                items += `
                    <li><a class="dropdown-item" href="${product_detail_url}">
                     <div class="d-flex w-100 justify-content-between">
                          <h5 class="mb-1">${product.name}</h5>
                          <small>3 days ago</small>
                        </div>
                        <p class="mb-1">${product.description}.</p>
                        <small>${product?.category.name}</small>
                    </a></li>
                `
            })
        }else{
            items += `
                <li><a class="dropdown-item text-muted" href="#">No results found</a></li>
            `
        }
        $('#search_items').html(items)
    },
    renderSearching: () => {
        let items = `
                <li><a class="dropdown-item text-muted" href="#">Searching ....</a></li>
            `
         $('#search_items').html(items)
    }
}

const { renderSearching, setProducts } = state


/**
 *  This loads data when page loads initially
 * */
SearchFunction('').then(r => setProducts(r)).catch(err => setProducts(err))


$('#search').on('keyup', (e) => {
    renderSearching()
    let value = e.target.value
    Debouncer(() => {
        SearchFunction(value)
            .then(r => {
                setProducts(r)
            })
            .catch(err => {
                setProducts(err)
            })
    }, 1000)()
})
