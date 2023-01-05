<template>
  <div ref="link" class="website">
    <button type="button" class="btn btn-primary" @click="getParentElement">Extract data</button>
    <button type="button" class="btn btn-danger" @click="clearAll">Clear all</button>
    <button type="button" class="btn btn-primary" @click="getParentElement">Get parent</button>

    <div ref="iframe" class="iframe my-4 rounded bg-white" @click="handleHover">
      <section class="col-12">
        <div class="row my-5">
          <div class="card">
            <div class="card-body">
              <p>Example</p>
              <ul>
                <li>Value A</li>
                <li>Value B</li>
              </ul>
              <div class="row">
                <div class="col-12">
                  <table class="table">
                    <thead>
                      <tr>
                        <th>Name</th>
                        <th>Age</th>
                      </tr>
                    </thead>
        
                    <tbody>
                      <tr>
                        <td>Kendall Jenner</td>
                        <td>25</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  data () {
    return {
      parentElement: null,
      selectedItem: null
    }
  },
  computed: {
    // parentValues () {
    //   if (this.selectedItem instanceof Element) {
    //     // If the selected item is a list, return the text of
    //     // all the similar elements within the inner parent
    //     if (this.selectedItem.localName === 'li') {
    //       const li = this.selectedItem.parentElement.querySelectorAll('li')
    //       return _.map(li, (element) => {
    //         return element.innerText
    //       })
    //     }

    //     if (this.selectedItem.localName === 'table') {
    //       const header = this.selectedItem.querySelector('thead')
    //       const body = this.selectedItem.querySelector('tbody')
    //       const headerValues = _.map(header.querySelectorAll('th'), (item) => {
    //         return item.innerText
    //       })
          
    //       const bodyValues = []
    //       _.forEach(body.querySelectorAll('tr'), (row) => {
    //         const rowValues = _.map(row.querySelectorAll('td'), (column) => {
    //           return column.innerText
    //         })
    //         bodyValues.push(rowValues)
    //       })
    //       return [headerValues, bodyValues]
    //     }
    //   }
    //   return []
    // }
  },
  methods: {
    handleHover (e) {
      // Select and highlight the element to parse
      this.selectedItem = document.elementFromPoint(e.clientX, e.clientY)
      if (this.selectedItem) {
        if (this.selectedItem.classList.contains('highlight')) {
          this.selectedItem.classList.remove('highlight')
        } else {
          this.selectedItem.classList.add('highlight')
        }
      }
    },
    clearAll () {
      this.parentElement = null
      this.selectedItem = null
      _.forEach(this.$refs.iframe.querySelectorAll('.highlight'), (element) => {
        element.classList.remove('highlight')
      })

      _.forEach(this.$refs.iframe.querySelectorAll('.highlight-parent'), (element) => {
        element.classList.remove('highlight-parent')
      })

    },
    getParentElement () {
      // Get the parent element of the 
      // currently selected item
      if (this.selectedItem) {
        const tableItems = ['tr', 'th', 'td']

        if (tableItems.includes(this.selectedItem.localName)) {
          this.parentElement = this.selectedItem.closest('table')
          this.parentElement.classList.add('highlight-parent')
        }
        
        const listItems = ['li']

        if (listItems.includes(this.selectedItem.localName)) {
          this.parentElement = this.selectedItem.closest('ul')
          this.parentElement.classList.add('highlight-parent')
        }
      }
    },
    selectSimilar () {
      // From a selected element on the page,
      // take all those who share similar
      // tag name or attributes e.g. id, class
      // based on the main parent
    }
  }
}
</script>

<style scoped>
.highlight {
  border-radius: .25em;
  background-color: rgba(46, 204, 113, .3);
  border: 1px solid rgba(46, 204, 113, .5);
  padding: 1rem
}

.highlight-parent {
  border-radius: .25em;
  background-color: rgba(192, 57, 43, .3);
  border: 1px solid rgba(192, 57, 43, .5);
  padding: 1rem
}

.iframe {
  height: 500px;
  overflow-y: scroll;
  padding: 2rem;
  box-shadow: inset 0 0 .8rem .25rem rgba(0, 0, 0, .075);
}

.iframe::-webkit-scrollbar {
  display: none;
}
</style>
