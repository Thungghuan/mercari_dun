function startDun() {
  console.log('开始蹲...')

  run()

  setInterval(run, 5000)
}

function run() {
  search().then((items) => {
    document.querySelector('.update-time').innerHTML = `最后更新时间：${(new Date()).toLocaleString()}`
    document.querySelector('.wrapper').innerHTML = ''
    items.map(update_item)
  })
}

async function search() {
  const input_el = document.querySelector('.keyword-input')
  const keyword = input_el.value
  console.log(input_el.value)

  const resp = await fetch('/search/' + keyword)
  const items = (await resp.json()).items.map((item) => ({
    buyer: item.buyerId,
    id: item.id,
    price: item.price,
    thumbnail: item.thumbnails[0]
  }))
  console.log(items)

  return items
}

function update_item(item) {
  const item_el = document.createElement('div')
  item_el.className = 'item-wrapper'
  item_el.innerHTML = `
    <div class="image-wrapper">
      <img src="${item.thumbnail}" class="thumbnail" />
    </div>
    <div class="text-wrapper">
      <div class="price${item.buyer === '' ? '' : ' sold'}">${item.price} => ${item.price * (item.price > 2000 ? 0.056 : 0.0565)}</div>
      <a class="link" href="https://jp.mercari.com/item/${item.id}" target="_blank">https://jp.mercari.com/item/${item.id}</a>
      <div class="buyer">buyer: ${item.buyer}</div>
    </div>
  `
  document.querySelector('.wrapper').appendChild(item_el)
}
