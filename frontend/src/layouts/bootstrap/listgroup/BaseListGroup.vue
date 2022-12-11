<template>
  <ul :class="listGroupClasses" class="list-group">
    <slot></slot>
  </ul>
</template>

<script>
export default {
  name: 'BaseListGroup',
  props: {
    color: {
      type: Boolean,
      default: null
    },
    horizontal: {
      type: Boolean
    },
    flush: {
      type: Boolean
    },
    numbered: {
      type: Boolean
    }
  },
  computed: {
    listGroupClasses () {
      return [
        {
          'list-group-flush': this.flush,
          'list-group-numbered': this.numbered,
          'list-group-horizontal': this.horizontal,
          [`list-group-item-${this.color}`]: true
        }
      ]
    }
  }
}
</script>
