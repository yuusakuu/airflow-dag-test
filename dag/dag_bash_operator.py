from __future__ import annotations

import datetime

import pendulum 
# datetime 을 더 사용하기 쉽게 만듬

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator", # 화면에서 보이는 이름, 파일명과 id를 일치시키는 것이 좋음
    schedule="0 0 * * *",  # cron 스케줄, 언제 도는지 설정, 분/시/일/월/요일 
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # 언제 부터 돌 것인가? / timezone = UTC, 한국보다 9시간 느림, 한국 시간 : Asia/Seoul
    catchup=False,  # false= 누락된 구간을 돌리지 않음 , true = 누락된 구간을 한꺼번에 돔 (일반적으로 false로 둔다)
    # dagrun_timeout=datetime.timedelta(minutes=60), # timeout 값을 설정,
    tags=["example", "example2"], # 어떤 값으로 설정할 것인가 태그를 달아줌
    # params={"example_key": "example_value"}, # dag 선언 밑에 태스크를 선언, 공통적으로 넘겨줄 것이라면 작성함
) as dag:
    # run_this_last = EmptyOperator(
    #     task_id="run_this_last",
    # )

    # # [START howto_operator_bash]
    # run_this = BashOperator(
    #     task_id="run_after_loop",
    #     bash_command="ls -alh --color=always / && echo https://airflow.apache.org/  && echo 'some <code>html</code>'",
    # )
    
    ##### bash 명과 task 아이디는 동일하게 설정하는게 편리
    bash_t1 = BashOperator(
        task_id = "bash_t1",
        bash_command = "echo whoami",  # string 출력, print 기능
    )
    bash_t2 = BashOperator(
        task_id = "bash_t2",
        bash_command = "echo $HOSTNAME",  # string 출력, print 기능
    )

    # 수행 순서 작성
    bash_t1 >> bash_t2 





    # [END howto_operator_bash]

    # run_this >> run_this_last

#     for i in range(3):
#         task = BashOperator(
#             task_id=f"runme_{i}",
#             bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
#         )
#         task >> run_this

#     # [START howto_operator_bash_template]
#     also_run_this = BashOperator(
#         task_id="also_run_this",
#         bash_command='echo "ti_key={{ task_instance_key_str }}"',
#     )
#     # [END howto_operator_bash_template]
#     also_run_this >> run_this_last

# # [START howto_operator_bash_skip]
# this_will_skip = BashOperator(
#     task_id="this_will_skip",
#     bash_command='echo "hello world"; exit 99;',
#     dag=dag,
# )
# # [END howto_operator_bash_skip]
# this_will_skip >> run_this_last

# if __name__ == "__main__":
#     dag.test()