const tag = document.querySelector('.tag')

function updateTag() {
  tag.innerHTML = `
  window.screen: ${window.width}, ${window.screen.height},
  window.outer: ${window.outerWidth}, ${window.outerHeight}
  window.inner: ${window.innerWidth}, ${window.innerHeight}
  document.clientWidth: ${document.documentElement.clientWidth}, ${document.documentElement.clientHeight}
  `
}

window.addEventListener('resize', () => {
  updateTag()
})
updateTag()