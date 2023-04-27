<template>
    <div class="text-h3 py-6 mx-10 text-left">{{ surname_s }} {{ name_s }} {{ patro_s }}</div>
    <div class="py-6 mx-10 d-flex justify-center" >
        <v-col>
            <v-card  class="my-2 pa-6 mx-14 d-flex flex-row">
                <b class="pr-2">Группа:</b>  {{ num_group }} 
                <v-spacer></v-spacer> 
                <b class="pr-2">Год поступления:</b>  {{ year_of_admission }} 
                <v-spacer></v-spacer>
                <b class="pr-2">Номер зачетки:</b>  {{ num_credit }} 
            </v-card>
        </v-col>
    </div>

    <div class="text-h5 py-6 mx-10 text-left">Список сдач</div>

    <div v-for="d in delivery" class="mx-15 d-flex justify-center" >
        <v-col>
            <v-card  class="pa-6 d-flex flex-row">
                <b class="pr-2">Дисциплина:</b>  {{ d.name_dis }} 
                <v-spacer></v-spacer> 
                <b class="pr-2">Название контроля:</b>  {{ d.name_control }} 
                <v-spacer></v-spacer>
                <b class="pr-2">Тема:</b>  {{ d.name_w }}
                <v-spacer></v-spacer>
                <b class="pr-2">Дата:</b>  {{ d.date_work }}
                <v-spacer></v-spacer>
                <b class="pr-2">Оценка:</b>  {{ d.score }}
                <v-spacer></v-spacer>
            </v-card>
            <v-card-actions class="mt-3">
                <v-spacer></v-spacer>
                <v-btn @click="delete_delivery(d)" variant="outlined" color="red"
                >Удалить</v-btn>
            </v-card-actions>
        </v-col>
    </div>

    <div>
        <v-row class="ma-14">
            <v-btn  block
                color="indigo"
                v-bind="props"
                :to="{ name: 'delivery', params: {num_credit:  this.$route.params.num_credit }}"
            >
                Добавить сдачу
            </v-btn>
        </v-row>
    </div>

</template>

<script>
import axios from 'axios';
import json from '@/data/students.json'


export default{
    data(){
        return{
            students: json,
            name_s: null,
            num_credit: null,
            num_group: null,
            patro_s: null,
            surname_s: null,
            year_of_admission: null,
            delivery: [],
            json: json
        }
    },
    updated(){
        this.get_data()
    },
    mounted(){
        this.get_data() 
    },
    methods: {
        get_data(){
            let student = this.students.find(item => item.num_credit == this.$route.params.num_credit)
            this.name_s = student.name_s
            this.num_credit = student.num_credit
            this.num_group = student.num_group
            this.patro_s = student.patro_s
            this.surname_s = student.surname_s
            this.year_of_admission = student.year_of_admission
            this.delivery = student.delivery
        },
        delete_delivery(d){
            for (let i=0; i<this.delivery.length; i++){
                if (this.delivery[i] == d){
                    this.delivery.splice(i,1)
                }
            }

            axios.post("http://127.0.0.1:5000/students", {
                students: this.students
            })
        }
    }
}
</script>