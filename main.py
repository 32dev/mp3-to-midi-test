# https://blog.naver.com/dev-32/224073599197
import os
from basic_pitch.inference import predict_and_save
# 💡 핵심: 최신 버전에서는 모델 객체나 경로를 명시적으로 전달해야 합니다.
from basic_pitch import ICASSP_2022_MODEL_PATH 

# --- 설정 ---
input_mp3 = r"practice-0001.mp3"  # 실제 MP3 파일 경로로 변경하세요
output_dir = r"output_midi_files"

# 출력 디렉터리 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 모델 경로 준비
basic_pitch_model_path = str(ICASSP_2022_MODEL_PATH)

# --- 변환 실행 (인수 추가) ---
predict_and_save(
    # 1. audio_paths: 입력 파일 목록
    [input_mp3], 
    
    # 2. output_directory: 출력 폴더
    output_dir, 
    
    # 3. save_model_outputs: (필수) 모델 출력을 저장할지 여부. 보통 False로 설정
    save_model_outputs=False, 
    
    # 4. save_notes: (필수) 음표 이벤트(MIDI)를 저장할지 여부.
    save_notes=True, 
    
    # 5. model_or_model_path: (필수) 사용할 모델의 경로 (여기서는 기본 모델 사용)
    model_or_model_path=basic_pitch_model_path,
    
    # save_midi, sonify_midi는 키워드 인수로 계속 사용할 수 있습니다.
    save_midi=True, # save_notes=True와 함께 사용되어 MIDI 파일 생성
    sonify_midi=False 
)
print(f"변환 완료. '{output_dir}' 폴더를 확인하세요.")