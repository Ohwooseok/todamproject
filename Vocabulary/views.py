from django.shortcuts import render
import json

# Create your views here.
from .models import wordlist

array = [
    
]

def study(request):
    return render(request, 'study.html')

def word(request):
    if request.method == 'GET':
        # 표시할 단어 개수
        amount = request.GET['amount']   
        # 단어장 배열
        arrays = wordlist.objects.all()
        return render(request, 'words.html', 
                    #   {'wordlists',arrays}
                    )

def test(request):
    return render(request, 'test.html')

def vocabulary(request):
    return render(request, 'vocabulary.html')


array = {
"keen "
:
"예리한"
,
"bookkeeper"
:
"회계 장부 담당자"
,
"difficulties"
:
"말썽, 곤란"
,
"causative"
:
"원인이 되는, 야기 시키는"
,
"affected"
:
"영향을 받는"
,
"athletics"
:
"체육, 육상 경기"
,
"affection"
:
"감정, 감동"
,
"marginal"
:
"최저의, 한계의"
,
"release"
:
"양도하다, 놓아주다"
,
"historic site"
:
"유적지"
,
"conduction"
:
"전도"
,
"even-numbered"
:
"짝수의"
,
"demonstration"
:
"입증, 설명, 시연"
,
"undisclosed"
:
"나타나지 않은"
,
"undetermined"
:
"미확인의"
,
"record"
:
"이력, 경력"
,
"association"
:
"협회, 연계, 연관"
,
"ballroom"
:
"무도회장"
,
"witness"
:
"직접보다, 목격하다"
,
"stringently"
:
"엄격하게, 용서 없이"
,
"bring together"
:
"모으다, 합치다"
,
"recognize"
:
"표창하다, 인정하다"
,
"expedition"
:
"여행, 탐험"
,
"remote"
:
"외딴, 외진"
,
"serve as"
:
"~의 역할을 하다"
,
"isolated"
:
"외딴, 고립된"
,
"vessel"
:
"선박, 배"
,
"therapeutic"
:
"치료법의"
,
"contraction"
:
"수축, 축소"
,
"metabolism"
:
"신진대사"
,
"possession"
:
"소유, 소지, 보유, 소지품"
,
"circular"
:
"원형의, 둥근, 순회하는"
,
"darken"
:
"어두워지다, 어둡게 만들다"
,
"mushroom"
:
"버섯, 급속히 늘어나다"
,
"bidding"
:
"(경매의) 가격 제시, 호가, 응찰"
,
"thoroughgoing"
:
"아주 철저한, 전면적인, 완전한"
,
"restrain"
:
"저지하다, 제지하다, 억누르다"
,
"acceptance"
:
"받아들임, 동의, 수락"
,
"hysterical"
:
"히스테리적인, 발작적인"
,
"certificate"
:
"증명, 증명서, 자격, 면허증"
,
"make time"
:
"서두르다, 빨리가다"
,
"princely"
:
"엄청난, 웅장한, 후한"
,
"religion"
:
"종교"
,
"attainment"
:
"성과, 성취, 달성"
,
"attached"
:
"애착을 가진, ~소속의"
,
"condense"
:
"응결되다, 압축시키다"
,
"achievement"
:
"업적, 성취한 것, 성취, 달성"
,
"defender"
:
"수비수, 옹호자"
,
"stay up"
:
"깨어있다, 안 자다"
,
"experienced"
:
"경험이 있는, 능숙한"
,
"subdue"
:
"진압하다, 가라앉히다, 억압하다"
,
"elementary"
:
"기본의, 초급의, 근본적인"
,
"fall out"
:
"헐거워지다, 해산하다"
,
"exclusion"
:
"제외, 배제, 차단"
,
"cuddle"
:
"껴안다, 포옹"
,
"divorced"
:
"이혼한, ~과 분리된, 단절된"
,
"inspiration"
:
"영감, 영감을 주는 사람"
,
"as an aside"
:
"작은 목소리로, 코멘트로서"
,
"magnetic"
:
"자성의, 자석 같은"
,
"skipper"
:
"선장, 주장"
,
"accelerate"
:
"가속화하다, 속도를 높이다"
,
"hereafter"
:
"이후로, 장차, 사후에"
,
"sort of"
:
"어느 정도, 다소, 뭐랄까"
,
"worthless"
:
"가치가 없는, 쓸모 없는"
,
"comparative"
:
"비교를 통한, 비교의, 상대적인"
,
"irrigate"
:
"물을 대다, 개관하다, 세척하다"
,
"facing"
:
"외장, 외관"
,
"choose sides"
:
"편을 짜다, 조를 정하다"
,
"surround"
:
"둘러싸다, 에워싸다, 포위하다"
,
"plainly"
:
"분명히, 숨김없이, 솔직히"
,
"individualism"
:
"개인주의, 개성"
,
"breadth"
:
"폭, 너비, 폭넓음"
,
"treasury"
:
"금고, 재무부"
,
"magician"
:
"마법사, 마술사"
,
"insure"
:
"보험에 들다, 보험을 팔다"
,
"signify"
:
"의미하다, 중요하다, 문제가 되다"
,
"strength"
:
"힘, 기운, 내구력, 견고성"
,
"spiral"
:
"나선, 나선형, 소용돌이"
,
"phonetic"
:
"목소리의, 음성을 나타내는"
,
"conductor"
:
"지휘자, 안내원"
,
"absurd"
:
"우스꽝스러운, 불합리, 부조리"
,
"for now"
:
"우선은, 현재로는, 당분간은"
,
"explosion"
:
"폭발, 폭파, 폭발적인 증가"
,
"vertical"
:
"수직, 수직의, 세로의"
,
"at a discount"
:
"할인하여, 경시되어(부당한 평가)"
,
"salute"
:
"경례를 하다, 절하다"
,
"concord"
:
"화합, 일치"
,
"husbandry"
:
"농사, 절약"
,
"thrill"
:
"황홀감, 흥분, 설렘, 전율"
,
"reasonably"
:
"꽤, 상당히, 합리적으로"
,
"conviction"
:
"유죄선고, 판결, 신념"
,
"feel sick"
:
"곧 토할 것 같다, 구역질이 나다"
,
"crater"
:
"분화구, 큰 구멍"
,
"payable"
:
"지불할 수 있는, 지불해야 하는"
,
"resignation"
:
"사직, 사임, 사직서"
,
"addition"
:
"덧셈, 추가된 것, 부가물"
,
"goodly"
:
"상당한, 잘생긴, 질 좋은"
,
"expectant"
:
"기대하는, 곧 부모가 될 사람"
,
"gossip"
:
"소문, 험담, 수다, 험담꾼"
,
"run against"
:
"~에 충돌하다, 우연히 만나다"
,
"dreadful"
:
"끔찍한, 지독한, 무시무시한"
,
"philosopher"
:
"철학자, 철학자 같은 사람"
,
"peculiarly"
:
"아주, 특히, 독특하게"
,
"wrestle"
:
"몸싸움을 하다, 레슬링을 하다"
,
"pop out"
:
"잠시 외출하다, 급사하다"
,
"portal"
:
"정문, 포털"
,
"ventilate"
:
"환기하다, 표명하다"
,
"eminence"
:
"명성, 예하, 고지, 언덕"
,
"convey"
:
"전달하다, 운송하다"
,
"bulwark"
:
"방어물, 보호자, 방어벽"
,
"sprint"
:
"전력 질주(하다), 단거리 경기"
,
"somersault"
:
"공중제비, 재주 넘기(하다)"
,
"checker"
:
"계산대 직원, 검사 프로그램"
,
"infuse"
:
"불어 넣다, 우리다"
,
"usher"
:
"정리, 안내하다, 좌석 안내원"
,
"moderate"
:
"사회를 보다, 적당한, 완화하다"
,
"conceit"
:
"자만, 자부심, 효과"
,
"maternity leave"
:
"출산 휴가"
,
"fabricate"
:
"위조하다, 제작하다, 조립하다"
,
"comprehensive"
:
"이해할 수 있는, 알기 쉬운"
,
"prospective buyer"
:
"잠재 구매자, 예상 구매자"
,
"accidently"
:
"우연히"
,
"brand-new"
:
"신상품의, 새 것, 신형의"
,
"reserved for"
:
"~을 위해 예약하다, 따로 두다"
,
"regular price"
:
"정가"
,
"installment"
:
"할부금, 할부, 회분"
,
"eco-friendly"
:
"친환경적인"
,
"get tired of"
:
"지치다, 싫증나다, 권태를 느끼다"
,
"sovereignty"
:
"자주, 주권, 자주권, 통치권"
,
"prosperous"
:
"번영한, 번창한, 성공한"
,
"nominate"
:
"추천하다, 지명하다, 후보에 오르다"
,
"verify"
:
"검증하다, 확인하다, 입증하다"
,
"further"
:
"더, 더 나아가, 더 멀리, 게다가"
,
"authentic"
:
"정확한, 실제의, 믿을 만한, 모사한"
,
"antibiotic"
:
"항생제, 항바이러스, 항생물질"
,
"commemorate"
:
"기념하다, 축하하다, 맞이하다"
,
"wholesale price"
:
"도매가"
,
"persist"
:
"계속하다,"
,
"apprehensive"
:
"걱정되는, 불안한, 신경 쓰이는"
,
"carriage"
:
"운반, 운송, 마차, 객차, 운반비"
,
"preemptive"
:
"선제의, 선수를 치는, 우선적인"
,
"rearing"
:
"키우다, 양육, 사육"
,
"interpreting"
:
"통역, 해석"
,
"circumstances"
:
"사정, 상황, 환경, 처지, 형편"
,
"stuck in traffic"
:
"교통체증"
,
"attribute"
:
"여기다, 따른, 때문이라 생각하다"
,
"regime"
:
"정권, 제도, 체제"
,
"figure out"
:
"알아내다, 생각해 내다, 계산하다"
,
"pessimistic"
:
"회의적인, 비관적인"
,
"incomparable"
:
"비교할 수 없는, 유례 없는"
,
"convince"
:
"확신시키다, 설득하다"
,
"restore"
:
"복구하다, 복원하다"
,
"incompatibility"
:
"상반, 불일치, 호환성이 없음"
,
"urgency"
:
"긴급함, 절박함"
,
"generate"
:
"창출하다, 발생시키다"
,
"revenue"
:
"수익, 세입"
,
"set aside"
:
"확보하다, 챙겨놓다"
,
"intense"
:
"강렬한, 치열한"
,
"concur"
:
"동의하다, 의견 일치를 보다"
,
"lessen"
:
"줄이다, 줄다"
,
"collapse"
:
"실패, 무너지다"
,
"incur"
:
"초래하다, 발생시키다"
,
"inessential"
:
"없어도 되는, 꼭 필요한 것이 아닌"
,
"assembly"
:
"의례, 집회, 조례 "
,
"readily"
:
"손쉽게"
,
"dissolve"
:
"녹다, 용해하다"
,
"absorb"
:
"흡수하다"
,
"negatively"
:
"부정적으로"
,
"utilize"
:
"이용하다, 활용하다"
,
"notable"
:
"눈에 띄는, 주목 할만한"
,
"suggest"
:
"암시하다, 시사하다"
,
"struggle"
:
"애쓰다, 발버둥치다"
,
"throughout the country"
:
"전국 각지의"
,
"individualism"
:
"개인주의, 개성"
,
"capitalism"
:
"자본주의"
,
"proposed"
:
"제안된"
,
"hasten"
:
"서두르다"
,
"entrepreneur"
:
"사업가, 기업가"
,
"fascinate"
:
"마음을 사로잡다, 매료시키다"
,
"sales associate"
:
"영업사원"
,
"supplies"
:
"용품, 저장품"
,
"specifics"
:
"세부사항"
,
"possessions"
:
"소지품, 가재도구"
,
"belongings"
:
"재산, 소유물, 소지품"
,
"earnings"
:
"소득, 수입, 수익"
,
"resources"
:
"자원"
,
"check out"
:
"(사실로) 확인되다"
,
"merely"
:
"그저, 단지, 고작"
,
"omission"
:
"생략, 빠짐, 누락"
,
"advantage"
:
"유리한 점, 이점, 장점"
,
"incidence"
:
"발생정도"
,
"estimate"
:
"추정, 추산, 견적서, 추산하다"
,
"unanticipated"
:
"기대하지 않은"
,
"predictable"
:
"예측할 수 있는, 너무 뻔한"
,
"publications"
:
"간행물, 출판물"
,
"multiple/numerous/a number of"
:
"많은, 다수의"
,
"prediction"
:
"예측, 예견"
,
"circumstance"
:
"환경, 상황, 정황"
,
"rigorous"
:
"철저한, 엄격한"
,
"transaction"
:
"거래, 매매, 처리"
,
"requirement"
:
"필요, 필요조건"
,
"accidental"
:
"우연한, 돌발적인"
,
"occasional"
:
"가끔의"
,
"without one's consent"
:
"~의 동의(승락) 없이"
,
"passionate speech"
:
"열정적인 연설"
,
"subscription"
:
"구독료"
,
"foreseeable"
:
"예측할 수 있는"
,
"considerable"
:
"상당한, 많은"
,
"responsive"
:
"즉각 반응하는, 관심을 보이는"
,
"attendance"
:
"참석, 출석"
,
"withdraw"
:
"인출하다, 취소하다"
,
"distributor"
:
"배급 업자, 판매 회사"
,
"pertinent"
:
"관련 있는, 적절한"
,
"introduction"
:
"채용, 도입"
,
"conflict resolution"
:
"분쟁 해결"
,
"priority"
:
"우선 사항, 우선권"
,
"inspection"
:
"검사, 사찰"
,
"inefficiency"
:
"비능률, 무능, 비능률적인 것"
,
"maximize"
:
"극대화하다, 최대한 활용하다"
,
"entrant"
:
"신입생, 참가자"
,
"disciplinary action"
:
"징계 조치"
,
"transmission"
:
"변속기"
,
"usage"
:
"사용, 용법"
,
"heavy industries"
:
"중공업"
,
"state-of-the-art"
:
"최첨단의, 최신식의"
,
"resign"
:
"사임하다, 물러나다"
,
"relieve"
:
"완화하다, 덜어주다"
,
"slightly"
:
"약간, 조금"
,
"advent"
:
"도래, 출현"
,
"trigger"
:
"방아쇠, 계기, 유발하다"
,
"investigation"
:
"수사, 조사"
,
"practice"
:
"관행, 관례"
,
"a majority of"
:
"다수의"
,
"merger"
:
"합병"
,
"concluder"
:
"종결자, 조약 체결자"
,
"brokerage"
:
"중개업, 중개 수수료"
,
"undertaking"
:
"일, 약속, 사업"
,
"advantageous"
:
"이로운, 유익한"
,
"intended"
:
"대상으로 삼은, 의도하는"
,
"beneficiary"
:
"수혜자, 수령인"
,
"aggravate"
:
"악화시키다"
,
"desperate"
:
"필사적인, 절실한"
,
"curtail"
:
"(비용을)절감하다, 축소시키다"
,
"fulfill"
:
"완수하다, 이행하다"
,
"drainage pipe"
:
"배수관"
,
"feasibility study"
:
"예비조사, 타당성조사"
,
"deputy"
:
"대리의, 대리인"
,
"renowned"
:
"유명한, 명성있는"
,
"emission"
:
"방출, 배출, 배출물"
,
"dedicated"
:
"헌신적인, 전념하는"
,
"thorough"
:
"빈틈없는, 꼼꼼한, 철저한"
,
"estimated"
:
"견적의, 어림잡은"
,
"accurate"
:
"정확한, 정밀한"
,
"expenditure"
:
"지출, 비용"
,
"authorize"
:
"재가하다, 결제하다, 위임하다"
,
"grant"
:
"승인하다, 허가하다"
,
"ordinarily"
:
"정상적으로, 대개는"
,
"technically"
:
"기술적으로, 엄밀히 따지면"
,
"comparatively"
:
"비교적, 비교해 보면"
,
"gardening"
:
"원예"
,
"shut off"
:
"끄다, 잠그다"
,
"external"
:
"외부의"
,
"tutoring session"
:
"개인 교습"
,
"consult"
:
"상담하다, 상의하다, 참고하다"
,
"particular"
:
"특별한, 특유의"
,
"formula"
:
"제조법, 방식"
,
"remain to be seen"
:
"두고 볼 일이다, 두고 봐야한다"
,
"congressperson"
:
"국회의원"
,
"influx"
:
"쇄도, 유입, 밀어닥침"
,
"convinced"
:
"확신을 가진, 신념 있는"
,
"circulate"
:
"순환하다, 유포하다"
,
"precisely"
:
"바로, 정확히, 정확하게"
,
"repeatedly"
:
"되풀이 하여, 여러 차례"
,
"fairly"
:
"상당히, 꽤"
,
"whereas"
:
"반면에"
,
"resignation"
:
"사직, 사임, 사직서"
,
"permanent"
:
"영구적인"
,
"generate"
:
"발생시키다, 만들어 내다"
,
"revealing"
:
"(흥미로운 사실을) 드러내는"
,
"deteriorating"
:
"악화중인, 악화되어 가고 있는"
,
"overtaking"
:
"추월, 앞지르기"
,
"discourage"
:
"막다, 의욕을 꺾다, 좌절시키다"
,
"unanimously"
:
"만장일치로"
,
"consecutively"
:
"연속하여, 연이어"
,
"remarkably"
:
"두드러지게, 현저하게"
,
"identically"
:
"꼭 같게, 동등하게"
,
"kitchen utensil"
:
"주방 기구"
,
"scenery"
:
"경치, 풍경, 무대"
,
"stationery store"
:
"문구점"
,
"intersection"
:
"교차로"
,
"basement floor"
:
"지하"
,
"rewarding"
:
"보람 있는, 돈을 많이 받는"
,
"specify"
:
"(구체적으로) 명시하다"
,
"exaggerate"
:
"과장하다"
,
"involvement"
:
"개입, 관여"
,
"disclose"
:
"발표하다, 공개하다"
,
"shareholder"
:
"주주"
,
"intention"
:
"의사, 의도, 목적"
,
"appropriation"
:
"도용, 전용, 책정"
,
"eliminate"
:
"제거하다"
,
"coincide with"
:
"~과 동시에 일어나다"
,
"reference"
:
"참고, 참조 "
,
"crucial"
:
"매우 중요한, 필수적인"
,
"inhabit"
:
"살다, 서식하다"
,
"ecosystem"
:
"생태계"
,
"dispatch"
:
"보내다, 파견하다"
,
"encounter"
:
"직면하다, 접하다"
,
"depression"
:
"우울증, 불황"
,
"transmit"
:
"발신하다, 전달하다"
,
"valuables"
:
"귀중품"
,
"terminate"
:
"끝나다, 종료되다"
,
"appealing"
:
"매력적인, 흥미로운"
,
"civil service"
:
"공무원"
,
"world-renowned"
:
"세계적으로 유명한"
,
"originality"
:
"독창성"
,
"handcraft"
:
"수공예"
,
"attention"
:
"정성, 배려"
,
"furnish A with B"
:
"A에게 B를 제공하다"
,
"range from A to B"
:
"A에서 B까지 이르다"
,
"be confronted with"
:
"~에 직면하다"
,
"inspiring"
:
"영감을 주는"
,
"orphanage"
:
"고아원"
,
"nonprofit"
:
"비영리의, 비영리 단체"
,
"the underprivileged"
:
"불우한 사람들"
,
"strengthen"
:
"강화하다, 더 튼튼해지다"
,
"administration"
:
"정부, 내각"
,
"exhausting"
:
"소모적인, 진을 빼는"
,
"exhaustion"
:
"소모, 고갈"
,
"registered"
:
"등록된, 공인된"
,
"retirement"
:
"연금, 퇴직"
,
"delegate"
:
"대표자, 위임하다, 뽑다"
,
"conclusion"
:
"판단, 결론, 결말, 체결"
,
"concluding"
:
"종결의, 최종의, 끝맺는"
,
"meet the requirements"
:
"조건을 충족시키다"
,
"outdated"
:
"시대에 뒤쳐진, 구식의"
,
"be packed with"
:
"~로 가득하다, 꽉 들어차다"
,
"initiate"
:
"시작하다, 개시하다"
,
"detector"
:
"감지기, 탐지기"
,
"component"
:
"구성요소, 부품"
,
"residence"
:
"주택, 거주지"
,
"prescription"
:
"처방, 처방전"
,
"the elderly"
:
"노인들"
,
"respondent"
:
"응답자"
,
"immigration"
:
"이민, 이주"
,
"publicist"
:
"홍보 담당자"
,
"instruction"
:
"교육, 훈련"
,
"permanent"
:
"정규직의, 영원한"
,
"necessary"
:
"필요한, 필연적인"
,
"file a complaint"
:
"항의를 제기하다"
,
"completed"
:
"작성한, 완료된"
,
"get along with"
:
"~와 잘 지내다"
,
"termination"
:
"종료"
,
"indicate"
:
"보이다, 가리키다"
,
"inaccuracy"
:
"오류, 틀림"
,
"registrant"
:
"등록자"
,
"board of directors"
:
"이사회"
,
"interpreter"
:
"통역사, 해석자"
,
"operator"
:
"운영자, 경영자"
,
"raw material"
:
"원자재, 원료"
,
"hazardous"
:
"위험한"
,
"strike"
:
"치다, 때리다, 파업"
,
"debate"
:
"토론, 토의, 논쟁, 논의하다"
,
"coverage"
:
"보도, 범위, 보급"
,
"conservation"
:
"보존, 보호, 관리"
,
"satisfaction"
:
"만족, 충족"
,
"negotiator"
:
"협상자, 교섭자"
,
"in general"
:
"전반적으로, 대체로, 보통"
,
"clothing"
:
"의류, 옷"
,
"relieved"
:
"안도하는, 다행으로 여기는"
,
"cuisine"
:
"요리, 요리법"
,
"transmission"
:
"전염, 송전, 전송, 방송"
,
"appreciate"
:
"좋게보다, 고마워하다, 인식하다"
,
"authority"
:
"권한, 권위, 지휘권, 인가"
,
"abstain from"
:
"삼가다, 그만두다"
,
"efficient"
:
"능률적인, 유능한"
,
"patron"
:
"후원자, 홍보대사, 고객"
,
"embark"
:
"착수하다, 승선하다"
,
"regimen"
:
"꾸준하고 엄한 훈련, 식이 요법"
,
"associate"
:
"동료, 친구, 연상하다, 어울리다"
,
"charitable"
:
"자비로운, 너그러운, 자선의"
,
"authorization"
:
"권한 부여, 허가, 허가증"
,
"forbid"
:
"~을 어렵게 하다, 금지하다"
,
"freeze"
:
"얼다, 얼리다, 동결"
,
"plagiarism"
:
"표절"
,
"currency"
:
"통화, 토용"
,
"shortfall"
:
"부족(량), 부족액"
,
"instability"
:
"불안정"
,
"anxiety"
:
"불안, 걱정, 걱정거리, 열망"
,
"exert"
:
"가하다, 행사하다, 분투하다"
,
"stun"
:
"기절시키다, 큰 감동을 주다"
,
"likelihood"
:
"있음직한, 가능성"
,
"proof"
:
"증거(물), 증명(서), 입증"
,
"subjective"
:
"주관적인, 마음속에 존재하는"
,
"pension"
:
"연금,생활 보조금, 수당"
,
"eligibleness"
:
"바람직함, 적격임"
,
"innovate"
:
"혁신하다, 도입하다"
,
"competent"
:
"능숙한, 만족할 만한, 권한이 있는"
,
"legalize"
:
"적법화하다, 합법화하다"
,
"legally"
:
"합법(법률)적으로, 법률상"
,
"reliability"
:
"신뢰도, 확실성"
,
"unwilling"
:
"꺼리는, 싫어하는, 본의 아닌"
,
"strategy"
:
"계획, 전략"
,
"mostly"
:
"주로, 일반적으로"
,
"award-winning"
:
"상을 받은"
,
"collecting"
:
"채집, 수집, 모금용의"
,
"perfection"
:
"완벽, 완성"
,
"compliancy"
:
"준수, 따름"
,
"reform"
:
"개선하다, 교화시키다, 교화하다"
,
"critically"
:
"비평적으로, 혹평하여, 위태롭게"
,
"acclaimed"
:
"호평을 받는, 칭찬을 받고 있는"
,
"attractively"
:
"보기 좋게, 매력적으로"
,
"personalize"
:
"표시하다, 맞추다, 개인화하다"
,
"personally"
:
"개인적으로, 직접"
,
"specifics"
:
"세부사항, 구체적인"
,
"unsound"
:
"부적절한, 견고하지 못한"
,
"substandard"
:
"표준 이하의, 열악한"
,
"admonish"
:
"꾸짖다, 책망하다, 충고하다"
,
"commodity"
:
"상품, 원자재, 농산물"
,
"devise"
:
"창안하다, 고안하다, 장치"
,
"allow for"
:
"감안하다, 잡아두다, 고려하다"
,
"go on strike"
:
"파업하다"
,
"eager"
:
"열성적인, 열렬한, 간절히 바라는"
,
"enthusiastic"
:
"열중하는, 열렬한, 열광적인"
,
"up-to-date"
:
"최신의, 최근의"
,
"aggressive"
:
"적극적인, 공격적인"
,
"exposition"
:
"전시회, 설명, 박람회"
,
"sizable"
:
"꽤 큰, 상당한 크기의"
,
"burdensome"
:
"부담스러운, 힘든"
,
"marvelous"
:
"훌륭한, 놀라운, 기적적인"
,
"suddenly"
:
"갑자기, 돌연히, 급작스럽게"
,
"prospective"
:
"차기의, 장래의, 유망한"
,
"reportable"
:
"보고 가치가있는, 보고할 수 있는"
,
"drafting"
:
"기안(방법), 제도, 선발"
,
"power outage"
:
"정전, 송전 정지"
,
"promptness"
:
"재빠름, 신속, 민첩성"
,
"progressive"
:
"진보적인, 점진적인, 진행되는"
,
"authorized"
:
"공인된, 인정받은, 권한을 받은"
,
"spring up"
:
"갑자기 생겨나다, 생기다"
,
"immediacy"
:
"직접성, 신속성, 속도"
,
"equality"
:
"평균, 균등"
,
"recognition"
:
"인식, 인정, 승인, 표창"
,
"simplicity"
:
"간단함, 평이함, 소박함"
,
"restructuring"
:
"기업 혁신 전략, 구조조정"
,
"incorporate"
:
"포함하다, 병합하다, 설립하다"
,
"real estate agent"
:
"부동산 중개인"
,
"extraction"
:
"뽑아냄, 추출"
,
"deposit"
:
"착수금, 보증금"
,
"precipitation"
:
"강수, 강수량, 침전"
,
"irreversible"
:
"돌이킬 수 없는, 철회할 수 없는"
,
"run through"
:
"~을 관통하다, 퍼지다, 넘치다"
,
"fixture"
:
"경기, 설치물, 고정물"
,
"in recognition of"
:
"~을 인정하여"
,
"push"
:
"밀다, 노력, 분발, 추진"
,
"mortgage"
:
"대출, 융자, 저당 잡히다"
,
"moderate"
:
"사회를 보다, 절제하다, 중간의"
,
"ethical"
:
"윤리적인, 도덕적인"
,
"contentment"
:
"만족(감), 흡족함"
,
"advocate"
:
"변호하다, 지지하다, 변호사"
,
"anniversary"
:
"기념일"
,
"within easy distance"
:
"가까운 거리에"
,
"dispute"
:
"분쟁, 논쟁, 이의를 제기하다"
,
"offense"
:
"공격적인, 무례, 불쾌한 것"
,
"regardful"
:
"주의 깊은, 유의하는, 용의주도한"
,
"prime"
:
"주된, 주요한, 최고의, 전성기"
,
"constraint"
:
"억압, 제약, 제한, 통제"
,
"genuine"
:
"진짜의, 진품의, 진품"
,
"reproduction"
:
"생식, 번식, 복제품, 복제"
,
"payroll"
:
"임금대장, 급여 지급"
,
"associated with"
:
"~와 관련된"
,
"entitle A to B"
:
"A에게 B의 자격을 주다"
,
"quota"
:
"할당량, 한도(량), 몫"
,
"commonplace"
:
"흔한, 보통의, 진부한 말"
,
"living standard"
:
"생활 수준"
,
"refurbish"
:
"새로 단장하다, 갈다"
,
"implement"
:
"시행하다, 도구"
,
"undercover"
:
"비밀의, 위장 근무의"
,
"in regard of"
:
"~에 관해서는"
,
"settlement"
:
"합의, 해결, 정착"
,
"intriguing"
:
"아주 흥미로운"
,
"house"
:
"집, 식구들, 수용하다"
,
"regional office"
:
"지사, 지방 관청"
,
"allowance"
:
"수당, 용돈, 허용량"
,
"sales representative"
:
"영업 담당자"
,
"incomplete"
:
"미완성의, 불충분한, 불완전한"
,
"infrastructure"
:
"기반, 사회(공공) 기반 시설"
,
"unmatched"
:
"상대가 없는, 타의 추종을 불허하는"
,
"registration form"
:
"신청서, 등기 용지"
,
"appliances"
:
"가전 제품"
,
"morale"
:
"사기, 의욕"
,
"overall"
:
"종합적으로, 전반적으로, 대체로"
,
"chief executive"
:
"최고 책임자"
,
"stimulate"
:
"자극하다, 흥미를 불러일으키다"
,
"dedication"
:
"전념, 헌신"
,
"loyalty"
:
"성실, 충실, 충성심"
,
"benefit"
:
"혜택, 이익, 수당, 자선 행사"
,
"shelter"
:
"거주지, 피신(대피), 피난처"
,
"severance package"
:
"퇴직금"
,
"accomplishment"
:
"성과, 업적(공적), 기량, 완수"
,
"refinance"
:
"재정을 재건하다, 차환하다"
,
"abundance"
:
"풍부, 풍성, 풍부함"
,
"lasting"
:
"영속적인, 지속적인"
,
"reassure"
:
"안심시키다"
,
"layoff"
:
"일시(정리)해고, 강제 해고"
,
"strategic"
:
"전략의, 전략적인"
,
"appropriate"
:
"알맞은, 도용하다, 책정하다"
,
"lackluster"
:
"광택이 없는, 혼탁한, 신통치 않은"
,
"switch over"
:
"바꾸다, 돌리다, 전환, 변환"
,
"make sense"
:
"의미가 통하다, 타당하다"
,
"operational"
:
"운영상의, 사용할 준비가 갖춰진"
,
"certify"
:
"증명하다, 보증하다"
,
"dietary supplement"
:
"건강 보조식품"
,
"physician"
:
"의사, 의료진"
,
"standing"
:
"고정적인, 서서하는, 지위, 평판"
,
"lucrative"
:
"수익성이 좋은"
,
"supplemental"
:
"보충의, 부록의, 추가"
,
"automotive"
:
"자동차의"
,
"appointment"
:
"약속, 임명, 지명"
,
"suitable"
:
"적합한, 적절한, 알맞은"
,
"negotiate"
:
"성사시키다, 협상하다(타결하다)"
,
"certified"
:
"보증된, 공인의, 면허증을 가진"
,
"institute"
:
"기관, 연구소, 도입하다, 시작하다"
,
"private"
:
"개인 소유의, 사적인, 전용의"
,
"corporation"
:
"기업, 회사, 조합, 법인"
,
"tuition"
:
"수업, 교습, 등록금, 수업료"
,
"formerly"
:
"이전에, 예전에"
,
"envelope"
:
"봉투, 비닐봉투"
,
"information packet"
:
"자료 묶음"
,
"outline"
:
"개요, 윤곽을 보여주다"
,
"overrun"
:
"급속히 퍼지다, 가득 차다"
,
"demonstrate"
:
"증거를 보여주다, 발휘하다"
,
"horticulture"
:
"원예, 원예학"
,
"compatible with"
:
"~와 양립할 수 있는"
,
"arena"
:
"경기장, 공연장, 무대"
,
"surveyor"
:
"측량사, 감정인, 감독관"
,
"draw up"
:
"작성하다, 만들다"
,
"alteration"
:
"변경, 수정, 변화, 개조"
,
"intervene"
:
"개입하다, 끼어들다"
,
"halt"
:
"멈추다, 중지시키다, 멈춤, 중단"
,
"downswing"
:
"하락, 위축"
,
"exceptional"
:
"아주 우수한, 특출한"
,
"senior"
:
"고위의, 성인을 위한, 선배"
,
"bound"
:
"꼭 ~할 것 같은, 얽매인, 해야 하는"
,
"get stuck"
:
"꼼짝 못하게 되다, 막히다"
,
"fill out"
:
"기입하다, 작성하다"
,
"stabilize"
:
"안정되다, 안정시키다, 고정되다"
,
"comfort"
:
"안락, 편안함, 위로, 편의 시설"
,
"participant"
:
"참가자, 참여자"
,
"exclusive"
:
"독점적인, 비개방적인, 배타적인"
,
"expansive"
:
"광활한, 광범위한, 포괄적인, 고가의"
,
"reproduce"
:
"복사하다, 다시 만들어내다,"
,
"clarity"
:
"명료성, 명확성, 선명도"
,
"steadily"
:
"착실하게, 꾸준하게, 끊임없이"
,
"expansion"
:
"확대, 확장, 팽창"
,
"matter"
:
"문제, 물질, 상황, 사정"
,
"provided"
:
"만약 ~라면"
,
"refute"
:
"반박하다, 부인하다"
,
"supplementary"
:
"추가의, 보충의"
,
"committee"
:
"위원회"
,
"allocate"
:
"할당하다, 분배하다"
,
"vice president"
:
"부통령, 부사장"
,
"divulge"
:
"알려주다, 누설하다"
,
"confidential"
:
"기밀의, 비밀의, 은밀한"
,
"remind"
:
"상기시키다, 다시 한 번 말해주다"
,
"determine"
:
"밝히다, 알아내다, 결정하다"
,
"disburse"
:
"지불하다, 지출하다, 분배하다"
,
"organize"
:
"조직하다, 정리하다, 체계화하다"
,
"spending"
:
"소비, 지출"
,
"inadvertently"
:
"무심코, 우연히, 부주의로"
,
"depending on"
:
"~에 따라, 따라서"
,
"implementation"
:
"실행, 이행, 완성, 성취"
,
"be loyal to"
:
"~에 충실하다, 의리를 지키다"
,
"hoist"
:
"끌어(들어)올리다, 승강장치"
,
"admittance"
:
"입원, 입장, 들어감, 인정"
,
"admittable"
:
"허용할 수 있는, 들어갈 자격이 있는"
,
"trustworthy"
:
"믿을 만한, 신뢰할 수 있는"
,
"corporate"
:
"기업의, 회사의, 조직의, 법인의"
,
"perceive"
:
"알아차리다, 인지하다, 여기다"
,
"when it comes to"
:
"~에 관해서는, ~에 관한 한"
,
"translation"
:
"통역, 번역, 번역문"
,
"fortune"
:
"재산, 부, 거금, 운수, 행운"
,
"circumstance"
:
"환경, 사정, 상황, 형편"
,
"enrollee"
:
"등록자, 가입자"
,
"inconvenience"
:
"불편, 애로, 불편한 사람"
,
"inability"
:
"무능, 불능, 할 수 없음"
,
"species"
:
"종"
,
"capable"
:
"유능한, 능력 있는"
,
"vegetation"
:
"초목, 식물"
,
"proportion"
:
"부분, 비율, 비, 균형"
,
"outreach"
:
"봉사 활동, 지원 활동"
,
"imperative"
:
"긴급한, 필수적인, 위엄 있는"
,
"enthusiasm"
:
"의욕, 열광, 열의, 열광하는 대상"
,
"regulation"
:
"규정, 규제, 통제, 단속"
,
"embassy"
:
"대사관"
,
"demanding"
:
"힘든, 부담이 큰, 요구가 많은"
,
"verify"
:
"확인하다, 입증하다, 진리, 진실"
,
"air ventilation"
:
"환기"
,
"in the long run"
:
"긴 안목으로 보면, 결국에, 대체로"
,
"specialized"
:
"전문적인, 전문화된"
,
"specialization"
:
"전문화, 특수화, 전문 분야"
,
"reimbursement"
:
"상환, 변제, 배상, 갚음"
,
}