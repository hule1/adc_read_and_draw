
#ifndef __EASYUSB_CARD_DLL__
#define __EASYUSB_CARD_DLL__


//#pragma comment(lib,"easyusb_card_dll.lib")
 
#ifdef __cplusplus
extern "C" {
#endif


// *********** �豸�򿪺������ɹ�����0 ***********
	int __stdcall OpenUsbV20(void);

// *********** �豸�رպ������ɹ�����0 ***********
	int __stdcall CloseUsbV20(void);

// *********** USB�豸���¹��غ������ɹ�����0��Ȼ����Ҫ���´��豸 ***********
	int __stdcall ResetUsbV20(void);

// *********** ��λ�豸�������ɹ�����0 ***********
	int __stdcall ResetUsbPipeV20(void);

// *********** ��ȡ�豸�����������ɹ�����0 ***********
	int __stdcall GetDeviceCountV20(void);

// *********** �л��豸�������ɹ�����0 ***********
	int __stdcall SetCurDeviceV20(int Devicenum);



// *********** ���λ�ȡAD�ɼ�������ɹ�����0 ***********
	int __stdcall ADSingleV20(int chan,float* adResult);

// *********** ��ͨ����ȡAD�ɼ�������ɹ�����0 ***********
	int __stdcall ADContinuV20(int chan,int Num_Sample,int Frequency,float  *databuf);

// *********** ��ȡ��ͨ��AD�ɼ�������ɹ�����0 ***********
	int __stdcall MADContinuV20(int chan_first,int chan_last,int Num_Sample,int Frequency,float  *mad_data);

// *********** DAͨ����ֵ������ɹ�����0 ***********
	int __stdcall DASingleOutV20(int chan,int value);

// *********** DAͨ��ɨ�����ݷ��ͣ��ɹ�����0 ***********
	int __stdcall DADataSendV20(int chan,int Num,int *databuf);

// *********** DAͨ��ɨ��������ã��ɹ�����0 ***********
	int __stdcall DAScanOutV20(int chan,int Freq,int scan_Num);

// *********** PWM������ã��ɹ�����0 ***********
	int __stdcall PWMOutSetV20(int chan,int Freq,float DutyCycle);

// *********** PWM�������ã��ɹ�����0 ***********
	int __stdcall PWMInSetV20(int mod);

// *********** PWM��������ȡ���ɹ�����0 ***********
	int __stdcall PWMInReadV20(float* Freq, int* DutyCycle);

// *********** �������������ã��ɹ�����0 ***********
	int __stdcall CountSetV20(int mod);

// *********** �����������ȡ���ɹ�����0 ***********
	int __stdcall CountReadV20(int* count);

// *********** ����������趨���ɹ�����0 ***********
	int __stdcall DoSetV20(unsigned char chan,unsigned char state);

// *********** �����������ȡ���ɹ�����0 ***********
	int __stdcall DiReadV20(unsigned char *value);

// *********** ��ȡ�豸ID�ţ��ɹ�����0 ***********
	unsigned int __stdcall GetCardIdV20(void);
#ifdef __cplusplus
}
#endif



#endif


