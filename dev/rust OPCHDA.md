---
date created: 2025-08-01 14:22
modified: 2025-09-09 21:39
---
- [[dev/dev languages/Rust]] [[OPCHDA]]
	- Voorlopig in Python behouden omdat een import van [[OPCHDA]] naar [[Parquet]] in minder dan een minuut voltooid is.
- Er zijn 3 crates:
	- winapi: 3th party
	- windows-sys
	- windows: zou een wrapper rond windows-sys zijn maar met extra features voor COM object interaction. (=official Microsoft API)
- ## info over de windows crate
	- [Calling your first COM API - Kenny Kerr](https://kennykerr.ca/rust-getting-started/calling-your-first-com-api.html)
	- ```rust
	  let uri = CreateUri(w!("http://kennykerr.ca"), Uri_CREATE_CANONICALIZE, 0)?;
	  ```
		- There's quite a lot going on here. The first parameter is actually a `PCWSTR`, representing a null-terminated wide string used by many Windows APIs. The `windows` crate provides the handy `w!` macro for creating a valid null-terminated wide string as a compile-time constant.
	-
	- The `windows` crate also provides the handy `h!` macro for creating an `HSTRING`, the string type used by WinRT APIs:

Dit werkt niet, maar ik krijg het niet opgelost.
 e regel in bold vraagt een *const PWSTR
  let hr = disp.GetIDsOfNames(
              &GUID::zeroed(), // IID of the interface you're working with, replace with actual IID
              **&PWSTR(ptr.as_ptr() as *mut _) as *const _,**
              rgsznames.len() as u32,
              LOCALE_USER_DEFAULT,
              &mut dispidmember,
          );
-
- Graybox gbhda_aw_x64.dll
	- CLSID\{84B7F48F-9803-4b2a-B63D-5CE649698C07}
-
- ```rust
  use std::{ptr, ffi::OsStr};
  use std::ffi::OsString;
  use std::iter::once;
  use windows::{
      Win32::System::Com::{
          CLSIDFromProgID, CoCreateInstance, CoInitialize, CoUninitialize, IDispatch,
          CLSCTX_LOCAL_SERVER, DISPPARAMS, VARIANT,
      },
      core::{HSTRING},
  };
  use windows::core::*;
  use std::os::windows::ffi::OsStrExt;
  use windows::core::PCWSTR;
  
  pub fn to_wide_string(string: &str) -> Vec<u16> {
      let result = OsStr::new(string).encode_wide().chain(Some(0).into_iter()).collect::<Vec<_>>();
      result
  }
  fn main() {
      unsafe {
          
          println!("Start");
          let _ = CoInitializeEx(None, COINIT_MULTITHREADED);
  
          let lpsz: HSTRING = HSTRING::from("Graybox.OPC.HDAWrapper");
          let rclsid_result = CLSIDFromString(&lpsz);
          println!("{:?}", rclsid_result);
          let rclsid = match rclsid_result {
              Ok(guid) => guid,
              Err(err) => {
                  panic!("Failed to get CLSID: {}", err);
              }
          };
          println!("{:?}", rclsid);
  
          let _p_server: *mut IUnknown = ptr::null_mut();
  
          let disp: IDispatch = match CoCreateInstance(&rclsid, None, CLSCTX_ALL) {
              Ok(disp) => disp,
              Err(_) => {
                  CoCreateInstance(&rclsid, None, CLSCTX_LOCAL_SERVER).expect("reason")
              },
          };
          println!("{:?}", disp);
  
          // Get the DISPID of the method you want to call
          const method_name: HSTRING = HSTRING::from("MethodName"); // Replace with actual method name
          let rgsznames = vec![method_name];
          let mut dispidmember = 0;
  
          let ptr = method_name.as_ptr();
          let hstring = HSTRING::from("method");
          let Y = PCWSTR::from_raw(hstring.as_ptr());
          let mut member: Vec<u16> = to_wide_string(name);
  
          let obj = CreateIn create_instance::<IDispatch>(&clsid)?;
          let hr = disp.GetIDsOfNames(
              &GUID::zeroed(), // IID of the interface you're working with, replace with actual IID
              &PWSTR(ptr.as_ptr() as *mut _) as *const _,
              rgsznames.len() as u32,
              LOCALE_USER_DEFAULT,
              &mut dispidmember,
          );
          if let Err(err) = hr {
              eprintln!("Failed to get DISPID: {:?}", err);
              return;
          }
  
          println!("DISPID: {}", dispidmember);
          const LOCALE_USER_DEFAULT: u32 = 0x400;
          let riid = GUID::zeroed();
          let hstring = HSTRING::from("Graybox.OPC.HDAWrapper");
          let rgsznames = PCWSTR::from_raw(hstring.as_ptr());
          let cnames = 1;
          let lcid = LOCALE_USER_DEFAULT;
          let mut dispidmember = 0;
  
          let x = disp.GetIDsOfNames(&riid, &rgsznames, cnames, lcid, &mut dispidmember);
          println!("{:?}", x);
  
  
      }
      fn convert_to_pcwstr(s: HSTRING) -> *const u16 {
          let wide_chars: Vec<u16> = OsString::from(s).encode_wide().chain(once(0)).collect();
          wide_chars.as_ptr()
      }
  }
  
  ```

## Logs
[[2025-10-27]]: Nog eens geprobeerd via verschillende AI tools, maar die krijgen het ook niet opgelost.