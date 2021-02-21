<template lang="html">
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item href="/">Orders</b-nav-item>
        <b-nav-item href="/create-menu/">Create Menu</b-nav-item>
        <b-nav-item href="/menu/2/">Order for Backend</b-nav-item>
        <b-nav-item href="/menu/3/">Order for Frontend</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <div class="container">
      <div class="row">
        <div class="col text-left">
          <h2>Today Orders</h2>

          <div class="col-md-12">
            <div class="overflow-auto">
              <b-pagination
                v-model="currentPage"
                :total-rows="rows"
                :per-page="perPage"
                aria-controls="my-table"
              ></b-pagination>
            </div>
            <p class="mt-3">Página: {{ currentPage }}</p>

            <b-table striped hover :items="orders" :fields="fields">
              <template v-slot:cell(user)="row">
                <p>{{row.item.user}}</p>
              </template>
              <template v-slot:cell(order)="row">
                <p>{{row.item.order}}</p>
              </template>
              <template v-slot:cell(specifications)="row">
                <p>{{row.item.specifications}}</p>
              </template>
            </b-table>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      perPage: 5,
      currentPage: 1,
      fields: [
        { key: 'user', label: 'User'},
        { key: 'option', label: 'Option'},
        { key: 'specifications', label: 'Specifications'},
      ],
      orders: [],
    }
  },
  methods: {

    getOrders () {
      const path = `http://0.0.0.0:8000/today_orders/`
      axios.get(path).then((response) => {
        this.orders = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  computed: {
    rows() {
      return this.orders.length
    }
  },
  created(){
    this.getOrders()
  }
}
</script>

<style lang="css" scoped>
</style>