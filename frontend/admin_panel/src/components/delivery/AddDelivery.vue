<template>
    <div class="text-h3 py-6 mx-10 text-left">Добавить сдачу для {{ name_s }} {{ patro_s }} {{ surname_s }}</div>

    <v-row class="d-flex justify-center my-5">
        <v-card v-show="add_workload" class="pa-6" color="green-accent-1">
            Сдача добавлена
        </v-card>
    </v-row>

    <div class="py-6 mx-10 d-flex justify-center">
        <v-col>
            <v-row class="ma-10" v-if="stage === 0">
                <v-radio-group v-model="name_dis">
                    <v-radio color="indigo"  v-for="d in disciplines"
                        :value="d.name_dis"
                        :label="`${d.name_dis}`"
                    >
                    </v-radio>                                 
                </v-radio-group>
            </v-row>

            <v-row class="ma-10" v-else-if="stage === 1">
                <v-radio-group v-model="name_control">
                    <v-radio color="indigo"  v-for="f in forms_of_work"
                        :value="f.name_control"
                        :label="`${f.name_control}`"
                    >
                    </v-radio>  
                </v-radio-group>
            </v-row>

            <v-row class="ma-10" v-else-if="stage === 2">
                <v-col>
                    <v-row>
                        <v-text-field v-model="name_w" type="text" label="Тема" color="indigo"></v-text-field>
                        <v-text-field v-model="date_work" type="date" label="Дата здачи" color="indigo"></v-text-field>
                        <v-text-field v-model="score" type="number" label="Оценка" color="indigo"></v-text-field>
                    </v-row>
                    <v-row class="mt-10">
                        <v-btn block color="indigo" @click="create_delivery">
                            Добавить сдачу
                        </v-btn>
                    </v-row>
                </v-col>


            </v-row>


            <v-row class="ma-10">
                <v-btn @click="exit_stage" color="gray" v-if="stage != 0 ">
                    Назад
                </v-btn>

                <v-spacer></v-spacer>
                <v-btn @click="enter_stage" color="indigo" v-if="stage !=2">
                    Вперед
                </v-btn>
            </v-row>
        </v-col>
    </div>
</template>

<script>
import axios from 'axios';
import students_json from '@/data/students.json'
import disciplines_json from '@/data/disciplines.json'


export default{
    data: () => ({
        name_s: "",
        patro_s: "",
        surname_s: "",
        add_workload: false,
        disciplines: disciplines_json,
        students: students_json,
        forms_of_work: [],
        delivery: [],

        stage: 0,

        num_dis: "",
        num_work: "",
        num_credit: "",
        name_w: "",
        date_work: "",
        score: "",
        name_dis: "",
        name_control: ""
    }),

    methods: {
        get_student(){
            let student = this.students.find(item => item.num_credit == this.$route.params.num_credit)
            this.name_s = student.name_s,
            this.patro_s = student.patro_s,
            this.surname_s = student.surname_s,
            this.num_credit = student.num_credit,
            this.delivery = student.delivery
        },

        get_froms_of_work(name_dis){
            let discipline = this.disciplines.find(item => item.name_dis == name_dis)
            this.forms_of_work = discipline.forms_of_work

        },

        create_delivery(){

            this.delivery.push({
               "date_work": this.date_work,
               "name_control": this.name_control,
               "name_dis": this.name_dis,
               "name_w": this.name_w,
               "score": this.score
            })

            axios.post("http://127.0.0.1:5000/students", {
                students: this.students
            })
        

            this.add_workload = true,
            this.stage = 0,
            this.score = "",
            this.date_work = "",
            this.name_w = "",
            this.num_dis = "",
            this.num_work = "",
            this.name_control = "",
            this.name_dis = ""
        },

        enter_stage(){
            if (this.stage === 0){
                this.get_froms_of_work(this.name_dis)
            }
            else if (this.stage === 0){
                this.add_workload = false
            }
            this.stage++
        },

        exit_stage(){
            this.stage--
        },
    },
    mounted(){
        this.get_student()
    }
}
</script>