<template>
  <!-- aria-hidden="true" -->
  <div :class="spinnerClasses" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
</template>

<script>
export default {
  name: 'BaseSpinner',
  props: {
    color: {
      type: String,
      default: 'light'
    },
    grow: {
      type: Boolean
    },
    size: {
      type: String,
      default: 'md'
    }
  },
  computed: {
    spinnerClasses () {
      return [
        {
          'spinner-border': !this.grow,
          'spinner-grow': this.grow,
          [`spinner-border-${this.size}`]: !this.grow,
          [`spinner-grow-${this.size}`]: this.grow,
          [`text-${this.color}`]: true
        }
      ]
    }
  }
}
</script>
