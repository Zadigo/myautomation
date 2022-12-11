<template>
  <li :class="{ disabled: item.disabled }" :aria-disabled="disabled" class="list-group-item">
    <slot></slot>
  </li>
</template>

<script>
export default {
  name: 'BaseListGroupItem',
  props: {
    // item: {
    //   type: Object,
    //   default () {
    //     return {}
    //   }
    // },
    disabled: {
      type: Boolean
    }
  }
}
</script>
