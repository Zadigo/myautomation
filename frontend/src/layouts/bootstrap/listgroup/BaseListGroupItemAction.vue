<template>
  <a href :class="{ active: selected }" :aria-current="selected" :aria-disabled="disabled" class="list-group-item list-group-item-action" @click.prevent="emitValue">
    <slot></slot>
  </a>
</template>

<script>
export default {
  name: 'BaseListGroupItemAction',
  props: {
    disabled: {
      type: Boolean
    }
  },
  emits: {
    'list-group-item-selected' () {
      return true
    }
  },
  data () {
    return {
      selected: false
    }
  },
  methods: {
    emitValue () {
      this.selected = !this.selected
      this.$emit('list-group-item-selected')
    }
  }
}
</script>
